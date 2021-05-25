#!/usr/bin/env python
import configparser
import glob
import pathlib
import sys
from array import array

import ROOT
from plot_helpers import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)


def plot_limit_compare(plot_config, times_xsec=False):
    """Makes Brazilian plots"""
    input_dict = process_input_compare(plot_config)
    set_style(plot_config)

    num_points = input_dict["num_limits"]
    input_collections = {}
    for i in range(10):
        input_name = "limits_compare_{}".format(i)
        if input_name in input_dict:
            input_collections[input_name] = {
                "name": input_dict[input_name + "_name"],
                "value": input_dict[input_name],
                "tgraph": ROOT.TGraph(num_points),
            }

    # set curve and band
    xs = input_dict["x_points"]
    for i in range(num_points):
        for single_input in input_collections.values():
            single_input["tgraph"].SetPoint(i, xs[i], single_input["value"][i])

    # plot ratio limit
    width = parse_int(plot_config, "PLOT", "canvas_width")
    height = parse_int(plot_config, "PLOT", "canvas_height")
    if width and height:
        plot_canvas = ROOT.TCanvas("c", "c", 100, 100, width, height)
    elif (not width) and (not height):
        plot_canvas = ROOT.TCanvas("c", "c", 100, 100, 600, 600)
    else:
        logging.warning(
            "You only specified width or height for the canvas, please check your settings. Using default (600, 600) this time."
        )
        plot_canvas = ROOT.TCanvas("c", "c", 100, 100, 600, 600)
    frame = plot_canvas.DrawFrame(1.4, 0.001, 4.1, 10)
    frame.GetXaxis().SetTitle(parse_str(plot_config, "PLOT", "x_title"))
    if times_xsec:
        frame.GetYaxis().SetTitle(parse_str(plot_config, "PLOT", "y_title_times_xsec"))
    else:
        frame.GetYaxis().SetTitle(parse_str(plot_config, "PLOT", "y_title"))
    y_min = parse_float(plot_config, "PLOT", "y_min")
    if y_min:
        frame.SetMinimum(y_min)
    y_max = parse_float(plot_config, "PLOT", "y_max")
    if not y_max:
        y_max = 0
        for single_input in input_collections.values():
            for ele in single_input["value"]:
                if y_max < ele:
                    y_max = ele
        y_max = y_max * 1.05
    frame.SetMaximum(y_max)
    frame.GetXaxis().SetLimits(min(input_dict["x_points"]), max(input_dict["x_points"]))

    for index, single_input in enumerate(input_collections.values()):
        single_input["tgraph"].SetLineColor(get_plot_color(index))
        single_input["tgraph"].SetLineWidth(3)
        single_input["tgraph"].Draw("SAME L")

    label_x = parse_float(plot_config, "PLOT", "atlas_label_x_cor")
    label_y = parse_float(plot_config, "PLOT", "atlas_label_y_cor")
    # plot label
    if parse_bool(plot_config, "PLOT", "plot_atlas_label"):
        plot_status = parse_str(plot_config, "PLOT", "plot_status")
        if not plot_status or plot_status == "none":
            pass
        elif plot_status == "preliminary":
            atlas_label(label_x, label_y, plot_status="Preliminary")
        elif plot_status == "internal":
            atlas_label(label_x, label_y, plot_status="Internal")
        elif plot_status == "wip":
            atlas_label(label_x, label_y, plot_status="Work in progress")
        else:
            logging.warning(
                "Unrecognized plot_status, please check! Skip label plotting."
            )
    if parse_bool(plot_config, "PLOT", "plot_atlas_lumi"):
        lumi = parse_str(plot_config, "INFO", "luminosity")
        energy = parse_float(plot_config, "INFO", "energy")
        lumi_y = parse_float(plot_config, "PLOT", "atlas_lumi_y_cor")
        atlas_draw_luminosity_fb(label_x, lumi_y, lumi, energy, color=1)
    if parse_bool(plot_config, "PLOT", "plot_atlas_process"):
        plot_process = parse_str(plot_config, "PLOT", "process")
        process_y = parse_float(plot_config, "PLOT", "atlas_process_y_cor")
        if plot_process is None:
            plot_process = ""
        atlas_draw_text(label_x, process_y, plot_process, size=0.037)
    # plot legend
    if parse_bool(plot_config, "PLOT", "plot_legend"):
        legend_x0 = parse_float(plot_config, "PLOT", "legend_x0")
        legend_y0 = parse_float(plot_config, "PLOT", "legend_y0")
        legend_x1 = parse_float(plot_config, "PLOT", "legend_x1")
        legend_y1 = parse_float(plot_config, "PLOT", "legend_y1")
        legend = ROOT.TLegend(legend_x0, legend_y0, legend_x1, legend_y1)
        legend.SetFillStyle(0)
        legend.SetBorderSize(0)
        legend.SetTextSize(0.041)
        legend.SetTextFont(42)
        for single_input in input_collections.values():
            legend.AddEntry(single_input["tgraph"], single_input["name"], "L")
        legend.Draw()

    ROOT.gPad.SetTicks(1, 1)
    frame.Draw("sameaxis")
    if parse_bool(plot_config, "PLOT", "log_x"):
        plot_canvas.SetLogx()
    if parse_bool(plot_config, "PLOT", "log_y"):
        plot_canvas.SetLogy()

    save_folder = parse_str(plot_config, "FILE", "save_folder")
    if not save_folder:
        save_folder = "./"
    pathlib.Path(save_folder).mkdir(parents=True, exist_ok=True)
    if not times_xsec:
        save_file = parse_str(plot_config, "FILE", "save_file")
        if not save_file:
            save_file = "UpperLimit"
    else:
        save_file = parse_str(plot_config, "FILE", "save_file_xsec")
        if not save_file:
            save_file = "UpperLimit_Xsec"
    save_format = parse_str_list(plot_config, "FILE", "save_format")
    if not save_format:
        save_format = ["png"]
    for cur_format in save_format:
        plot_canvas.SaveAs(save_folder + "/" + save_file + "." + cur_format)
    plot_canvas.Close()


def set_style(plot_config):
    """Set styles for plotting
    
    Availabe styles:
        Classic(default), Plain, Bold, Video, Pub, Modern, ATLAS BELLE2
    
    """
    use_style = plot_config.get("PLOT", "style")
    if use_style:
        ROOT.gROOT.SetStyle(use_style)
    else:
        logging.warning("No style specified!")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        logging.critical("Missing config file!")
        exit()
    plot_config = configparser.RawConfigParser()
    plot_config.read(sys.argv[1])

    plot_limit_compare(plot_config, times_xsec=False)
    if parse_bool(plot_config, "PLOT", "plot_xsec"):
        plot_limit_compare(plot_config, times_xsec=True)
