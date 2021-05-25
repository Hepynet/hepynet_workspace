#include "NtupleMaker.h"

void string_replace(std::string &strBig, const std::string &strsrc, const std::string &strdst) {
    std::string::size_type pos = 0;
    std::string::size_type srclen = strsrc.size();
    std::string::size_type dstlen = strdst.size();

    while ((pos = strBig.find(strsrc, pos)) != std::string::npos) {
        strBig.replace(pos, srclen, strdst);
        pos += dstlen;
    }
}
std::string GetPathOrURLShortName(std::string strFullName) {
    if (strFullName.empty()) {
        return "";
    }

    string_replace(strFullName, "/", "\\");

    std::string::size_type iPos = strFullName.find_last_of('\\') + 1;

    return strFullName.substr(iPos, strFullName.length() - iPos);
}

double CaldPhi(double phi1, double phi2) {
    double Dphi = 0;
    Dphi = phi1 - phi2;
    if (fabs(Dphi) > Pi) {
        if (Dphi > 0) {
            Dphi = 2 * Pi - Dphi;
        } else {
            Dphi = 2 * Pi + Dphi;
        }
    }
    return Dphi;
}

double NtupleMaker::Lum(string INST) {
    if (INST.find("364156") != string::npos) mcChannelNumber = 364156;
    if (INST.find("364157") != string::npos) mcChannelNumber = 364157;
    if (INST.find("364158") != string::npos) mcChannelNumber = 364158;
    if (INST.find("364159") != string::npos) mcChannelNumber = 364159;
    if (INST.find("364160") != string::npos) mcChannelNumber = 364160;
    if (INST.find("364161") != string::npos) mcChannelNumber = 364161;
    if (INST.find("364162") != string::npos) mcChannelNumber = 364162;
    if (INST.find("364163") != string::npos) mcChannelNumber = 364163;
    if (INST.find("364164") != string::npos) mcChannelNumber = 364164;
    if (INST.find("364165") != string::npos) mcChannelNumber = 364165;
    if (INST.find("364166") != string::npos) mcChannelNumber = 364166;
    if (INST.find("364167") != string::npos) mcChannelNumber = 364167;
    if (INST.find("364168") != string::npos) mcChannelNumber = 364168;
    if (INST.find("364169") != string::npos) mcChannelNumber = 364169;
    if (INST.find("364170") != string::npos) mcChannelNumber = 364170;
    if (INST.find("364171") != string::npos) mcChannelNumber = 364171;
    if (INST.find("364172") != string::npos) mcChannelNumber = 364172;
    if (INST.find("364173") != string::npos) mcChannelNumber = 364173;
    if (INST.find("364174") != string::npos) mcChannelNumber = 364174;
    if (INST.find("364175") != string::npos) mcChannelNumber = 364175;
    if (INST.find("364176") != string::npos) mcChannelNumber = 364176;
    if (INST.find("364177") != string::npos) mcChannelNumber = 364177;
    if (INST.find("364178") != string::npos) mcChannelNumber = 364178;
    if (INST.find("364179") != string::npos) mcChannelNumber = 364179;
    if (INST.find("364180") != string::npos) mcChannelNumber = 364180;
    if (INST.find("364181") != string::npos) mcChannelNumber = 364181;
    if (INST.find("364182") != string::npos) mcChannelNumber = 364182;
    if (INST.find("364183") != string::npos) mcChannelNumber = 364183;
    if (INST.find("364184") != string::npos) mcChannelNumber = 364184;
    if (INST.find("364185") != string::npos) mcChannelNumber = 364185;
    if (INST.find("364186") != string::npos) mcChannelNumber = 364186;
    if (INST.find("364187") != string::npos) mcChannelNumber = 364187;
    if (INST.find("364188") != string::npos) mcChannelNumber = 364188;
    if (INST.find("364189") != string::npos) mcChannelNumber = 364189;
    if (INST.find("364190") != string::npos) mcChannelNumber = 364190;
    if (INST.find("364191") != string::npos) mcChannelNumber = 364191;
    if (INST.find("364192") != string::npos) mcChannelNumber = 364192;
    if (INST.find("364193") != string::npos) mcChannelNumber = 364193;
    if (INST.find("364194") != string::npos) mcChannelNumber = 364194;
    if (INST.find("364195") != string::npos) mcChannelNumber = 364195;
    if (INST.find("364196") != string::npos) mcChannelNumber = 364196;
    if (INST.find("364197") != string::npos) mcChannelNumber = 364197;
    if (INST.find("361106") != string::npos) mcChannelNumber = 361106;
    if (INST.find("361107") != string::npos) mcChannelNumber = 361107;
    if (INST.find("361108") != string::npos) mcChannelNumber = 361108;
    if (INST.find("410470") != string::npos) mcChannelNumber = 410470;
    if (INST.find("410471") != string::npos) mcChannelNumber = 410471;
    if (INST.find("410472") != string::npos) mcChannelNumber = 410472;
    if (INST.find("410644") != string::npos) mcChannelNumber = 410644;
    if (INST.find("410645") != string::npos) mcChannelNumber = 410645;
    if (INST.find("410646") != string::npos) mcChannelNumber = 410646;
    if (INST.find("410647") != string::npos) mcChannelNumber = 410647;
    if (INST.find("410658") != string::npos) mcChannelNumber = 410658;
    if (INST.find("410659") != string::npos) mcChannelNumber = 410659;
    if (INST.find("364250") != string::npos) mcChannelNumber = 364250;
    if (INST.find("364253") != string::npos) mcChannelNumber = 364253;
    if (INST.find("364254") != string::npos) mcChannelNumber = 364254;
    if (INST.find("364255") != string::npos) mcChannelNumber = 364255;
    if (INST.find("363355") != string::npos) mcChannelNumber = 363355;
    if (INST.find("363356") != string::npos) mcChannelNumber = 363356;
    if (INST.find("363357") != string::npos) mcChannelNumber = 363357;
    if (INST.find("363358") != string::npos) mcChannelNumber = 363358;
    if (INST.find("363359") != string::npos) mcChannelNumber = 363359;
    if (INST.find("363360") != string::npos) mcChannelNumber = 363360;
    if (INST.find("363489") != string::npos) mcChannelNumber = 363489;

    if (INST.find("402970") != string::npos) mcChannelNumber = 402970;
    if (INST.find("402975") != string::npos) mcChannelNumber = 402975;
    if (INST.find("402985") != string::npos) mcChannelNumber = 402985;
    if (INST.find("402995") != string::npos) mcChannelNumber = 402995;
    if (INST.find("403000") != string::npos) mcChannelNumber = 403000;
    if (INST.find("403010") != string::npos) mcChannelNumber = 403010;
    if (INST.find("403020") != string::npos) mcChannelNumber = 403020;
    if (INST.find("403025") != string::npos) mcChannelNumber = 403025;
    if (INST.find("403035") != string::npos) mcChannelNumber = 403035;
    if (INST.find("403022") != string::npos) mcChannelNumber = 403022;
    if (INST.find("402997") != string::npos) mcChannelNumber = 402997;
    if (INST.find("402972") != string::npos) mcChannelNumber = 402972;
    if (INST.find("403005") != string::npos) mcChannelNumber = 403005;
    if (INST.find("402980") != string::npos) mcChannelNumber = 402980;
    if (INST.find("403030") != string::npos) mcChannelNumber = 403030;
    if (INST.find("312428") != string::npos) mcChannelNumber = 312428;
    if (INST.find("312429") != string::npos) mcChannelNumber = 312429;
    if (INST.find("312430") != string::npos) mcChannelNumber = 312430;
    if (INST.find("312431") != string::npos) mcChannelNumber = 312431;
    if (INST.find("312432") != string::npos) mcChannelNumber = 312432;
    if (INST.find("312433") != string::npos) mcChannelNumber = 312433;
    if (INST.find("312434") != string::npos) mcChannelNumber = 312434;
    if (INST.find("312435") != string::npos) mcChannelNumber = 312435;
    if (INST.find("312436") != string::npos) mcChannelNumber = 312436;
    if (INST.find("312860") != string::npos) mcChannelNumber = 312860;
    if (INST.find("312863") != string::npos) mcChannelNumber = 312863;
    if (INST.find("312861") != string::npos) mcChannelNumber = 312861;
    if (INST.find("312862") != string::npos) mcChannelNumber = 312862;
    if (INST.find("312864") != string::npos) mcChannelNumber = 312864;
    if (INST.find("312865") != string::npos) mcChannelNumber = 312865;

    if ((INST.find("MC1516") != string::npos) || (INST.find("MC16a") != string::npos)) {
        //        lum =36.207660;
        luminosity = 3.219 + 32.988;
        //        Yeard =16;
    } else if ((INST.find("MC16d") != string::npos) || (INST.find("mc16d") != string::npos)) {
        //        lum =44.3074;
        luminosity = 44.307;
        //        Yeard = 17;
    } else if ((INST.find("MC16e") != string::npos) || (INST.find("mc16e") != string::npos)) {
        //        lum =59.9372;
        luminosity = 58.450;
        //        Yeard = 18;
    } else {
        cout << "MCSample Not 16a 16d or 16e" << endl;
    }
    return luminosity;
}

NtupleMaker::NtupleMaker(string Input, bool SampleType) {
    //    int Yeard = -1;
    //    wrkarea = "/eos/user/j/jugao/LFVWORK/SkimedRoot/1516/";
    TH1::SetDefaultSumw2();
    string Inos;
    ifstream os;
    isData = SampleType;
    os.open(Input.c_str());

    while (os >> Inos) {
        InputFileList.push_back(Inos);
    }
    if ((Input.length() > 20) || Input.find("/") != string::npos) {
        Input = GetPathOrURLShortName(Input);
    }
    filename = 0;
    Input.erase(Input.length() - 5);
    OutPutName = Input;

    //    cout<<Input<<endl;
    //    luminosity = 43813.7*0.001;
    NormSF = 1;
}

void NtupleMaker::ReadTreeLFVO(TChain *chain) {
    //    TFile *f1 = (TFile *)gROOT->GetListOfFiles()->FindObject((inFileName).c_str());
    //    TFile *f1 = new TFile(inFileName.c_str(),"READ");
    //    ssTree = (TTree *)f1->Get("LFV");
    //    chain->SetBranchAddress("PrwWeight",&(PrwWeight));

    chain->SetBranchAddress("weight_mc", &(weight_mc));
    chain->SetBranchAddress("weight_pileup", &(weight_pileup));
    chain->SetBranchAddress("weight_leptonSF", &(weight_leptonSF));
    chain->SetBranchAddress("weight_tauSF", &(weight_tauSF));
    chain->SetBranchAddress("weight_bTagSF_DL1r_77", &(weight_bTagSF_DL1r_77));
    chain->SetBranchAddress("weight_bTagSF_DL1r_85", &(weight_bTagSF_DL1r_85));
    chain->SetBranchAddress("weight_globalLeptonTriggerSF", &(weight_globalLeptonTriggerSF));
    chain->SetBranchAddress("weight_jvt", &(weight_jvt));
    chain->SetBranchAddress("eventNumber", &(eventNumber));
    chain->SetBranchAddress("runNumber", &(runNumber));
    chain->SetBranchAddress("randomRunNumber", &(randomRunNumber));
    chain->SetBranchAddress("mcChannelNumber", &(mcChannelNumber));
    chain->SetBranchAddress("mu", &(mu));
    chain->SetBranchAddress("mu_actual", &(mu_actual));
    chain->SetBranchAddress("backgroundFlags", &(backgroundFlags));
    chain->SetBranchAddress("hasBadMuon", &(hasBadMuon));
    chain->SetBranchAddress("el_pt", &(Ele_pt));
    chain->SetBranchAddress("el_eta", &(Ele_eta));
    chain->SetBranchAddress("el_cl_eta", &(el_cl_eta));
    chain->SetBranchAddress("el_phi", &(Ele_phi));
    chain->SetBranchAddress("el_e", &(Ele_e));
    chain->SetBranchAddress("el_charge", &(el_charge));
    chain->SetBranchAddress("el_topoetcone20", &(el_topoetcone20));
    chain->SetBranchAddress("el_ptvarcone20", &(el_ptvarcone20));
    chain->SetBranchAddress("el_CF", &(el_CF));
    chain->SetBranchAddress("el_d0sig", &(el_d0sig));
    chain->SetBranchAddress("el_delta_z0_sintheta", &(el_delta_z0_sintheta));
    chain->SetBranchAddress("el_true_type", &(el_true_type));
    chain->SetBranchAddress("el_true_origin", &(el_true_origin));
    chain->SetBranchAddress("el_true_firstEgMotherTruthType", &(el_true_firstEgMotherTruthType));
    chain->SetBranchAddress("el_true_firstEgMotherTruthOrigin", &(el_true_firstEgMotherTruthOrigin));
    chain->SetBranchAddress("el_true_firstEgMotherPdgId", &(el_true_firstEgMotherPdgId));
    chain->SetBranchAddress("el_true_isPrompt", &(el_true_isPrompt));
    chain->SetBranchAddress("el_true_isChargeFl", &(el_true_isChargeFl));
    chain->SetBranchAddress("mu_pt", &(Mu_pt));
    chain->SetBranchAddress("mu_eta", &(Mu_eta));
    chain->SetBranchAddress("mu_phi", &(Mu_phi));
    chain->SetBranchAddress("mu_e", &(Mu_e));
    chain->SetBranchAddress("mu_charge", &(mu_charge));
    chain->SetBranchAddress("mu_topoetcone20", &(mu_topoetcone20));
    chain->SetBranchAddress("mu_ptvarcone30", &(mu_ptvarcone30));
    chain->SetBranchAddress("mu_d0sig", &(mu_d0sig));
    chain->SetBranchAddress("mu_delta_z0_sintheta", &(mu_delta_z0_sintheta));
    chain->SetBranchAddress("mu_true_type", &(mu_true_type));
    chain->SetBranchAddress("mu_true_origin", &(mu_true_origin));
    chain->SetBranchAddress("mu_true_isPrompt", &(mu_true_isPrompt));
    chain->SetBranchAddress("tau_pt", &(Tau_pt));
    chain->SetBranchAddress("tau_eta", &(Tau_eta));
    chain->SetBranchAddress("tau_phi", &(Tau_phi));
    chain->SetBranchAddress("tau_charge", &(tau_charge));
    chain->SetBranchAddress("jet_pt", &(jet_pt));
    chain->SetBranchAddress("jet_eta", &(jet_eta));
    chain->SetBranchAddress("jet_phi", &(jet_phi));
    chain->SetBranchAddress("jet_e", &(jet_e));
    chain->SetBranchAddress("jet_mv2c10", &(jet_mv2c10));
    chain->SetBranchAddress("jet_DL1r", &(jet_DL1r));
    chain->SetBranchAddress("jet_jvt", &(jet_jvt));
    chain->SetBranchAddress("jet_passfjvt", &(jet_passfjvt));
    chain->SetBranchAddress("met_met", &(MET_met));
    chain->SetBranchAddress("met_phi", &(MET_phi));
    chain->SetBranchAddress("emuSelection", &(emuSelection));
    chain->SetBranchAddress("etauSelection", &(etauSelection));
    chain->SetBranchAddress("mutauSelection", &(mutauSelection));
    chain->SetBranchAddress("HLT_mu50", &(HLT_mu50));
    chain->SetBranchAddress("HLT_mu26_ivarmedium", &(HLT_mu26_ivarmedium));
    chain->SetBranchAddress("HLT_e140_lhloose_nod0", &(HLT_e140_lhloose_nod0));
    chain->SetBranchAddress("HLT_e26_lhtight_nod0_ivarloose", &(HLT_e26_lhtight_nod0_ivarloose));
    chain->SetBranchAddress("HLT_e120_lhloose", &(HLT_e120_lhloose));
    chain->SetBranchAddress("HLT_mu20_iloose_L1MU15", &(HLT_mu20_iloose_L1MU15));
    chain->SetBranchAddress("HLT_e24_lhmedium_L1EM20VH", &(HLT_e24_lhmedium_L1EM20VH));
    chain->SetBranchAddress("HLT_e60_lhmedium", &(HLT_e60_lhmedium));
    chain->SetBranchAddress("HLT_e60_lhmedium_nod0", &(HLT_e60_lhmedium_nod0));
    chain->SetBranchAddress("el_trigMatch_HLT_e60_lhmedium_nod0", &(el_trigMatch_HLT_e60_lhmedium_nod0));
    chain->SetBranchAddress("el_trigMatch_HLT_e60_lhmedium", &(el_trigMatch_HLT_e60_lhmedium));
    chain->SetBranchAddress("el_trigMatch_HLT_e24_lhmedium_L1EM20VH", &(el_trigMatch_HLT_e24_lhmedium_L1EM20VH));
    chain->SetBranchAddress("el_trigMatch_HLT_e120_lhloose", &(el_trigMatch_HLT_e120_lhloose));
    chain->SetBranchAddress("el_trigMatch_HLT_e26_lhtight_nod0_ivarloose",
                            &(el_trigMatch_HLT_e26_lhtight_nod0_ivarloose));
    chain->SetBranchAddress("el_trigMatch_HLT_e140_lhloose_nod0", &(el_trigMatch_HLT_e140_lhloose_nod0));
    chain->SetBranchAddress("mu_trigMatch_HLT_mu50", &(mu_trigMatch_HLT_mu50));
    chain->SetBranchAddress("mu_trigMatch_HLT_mu20_iloose_L1MU15", &(mu_trigMatch_HLT_mu20_iloose_L1MU15));
    chain->SetBranchAddress("mu_trigMatch_HLT_mu26_ivarmedium", &(mu_trigMatch_HLT_mu26_ivarmedium));
    chain->SetBranchAddress("weight_KFactor", &(weight_KFactor));
    chain->SetBranchAddress("mu_isHighPt", &(mu_isHighPt));
    chain->SetBranchAddress("mu_isolation_FixedCutTight", &(mu_isolation_FixedCutTight));
    chain->SetBranchAddress("mu_isolation_FixedCutLoose", &(mu_isolation_FixedCutLoose));
    chain->SetBranchAddress("el_isolation_FixedCutLoose", &(el_isolation_FixedCutLoose));
    chain->SetBranchAddress("el_isolation_FixedCutTight", &(el_isolation_FixedCutTight));
    chain->SetBranchAddress("el_isElTight", &(el_isElTight));
    chain->SetBranchAddress("el_isElMedium", &(el_isElMedium));
    chain->SetBranchAddress("el_isElLoose", &(el_isElLoose));
    chain->SetBranchAddress("tau_isBDTTight", &(tau_isBDTTight));
    chain->SetBranchAddress("tau_isBDTMedium", &(tau_isBDTMedium));
    chain->SetBranchAddress("tau_isBDTLoose", &(tau_isBDTLoose));
    chain->SetBranchAddress("tau_isRNNTight", &(tau_isRNNTight));
    chain->SetBranchAddress("tau_isRNNMedium", &(tau_isRNNMedium));
    chain->SetBranchAddress("tau_isRNNLoose", &(tau_isRNNLoose));
    chain->SetBranchAddress("tau_RNNScore", &(tau_RNNScore));
    chain->SetBranchAddress("tau_nTracks", &(tau_nTracks));
    chain->SetBranchAddress("jet_isbtagged_DL1r_77", &(jet_isbtagged_DL1r_77));
    chain->SetBranchAddress("jet_isbtagged_DL1r_85", &(jet_isbtagged_DL1r_85));
}

double NtupleMaker::FindXsec(double mcChannelNumber) {
    double XSEC = 1;
    if (mcChannelNumber == 364156.0)
        XSEC = 19151.0E+03 * 0.8246 * 0.9702;
    else if (mcChannelNumber == 364157.0)
        XSEC = 19145.0E+03 * 0.13031 * 0.9702;
    else if (mcChannelNumber == 364158.0)
        XSEC = 19143.0E+03 * 0.044209 * 0.9702;
    else if (mcChannelNumber == 364159.0)
        XSEC = 945.89E+03 * 0.6815 * 0.9702;
    else if (mcChannelNumber == 364160.0)
        XSEC = 946.12E+03 * 0.23841 * 0.9702;
    else if (mcChannelNumber == 364161.0)
        XSEC = 944.95E+03 * 0.084077 * 0.9702;
    else if (mcChannelNumber == 364162.0)
        XSEC = 339.73E+03 * 0.60009 * 0.9702;
    else if (mcChannelNumber == 364163.0)
        XSEC = 339.8E+03 * 0.29172 * 0.9702;
    else if (mcChannelNumber == 364164.0)
        XSEC = 339.68E+03 * 0.1111 * 0.9702;
    else if (mcChannelNumber == 364165.0)
        XSEC = 72.084E+03 * 0.54766 * 0.9702;
    else if (mcChannelNumber == 364166.0)
        XSEC = 72.103E+03 * 0.32005 * 0.9702;
    else if (mcChannelNumber == 364167.0)
        XSEC = 72.063E+03 * 0.13137 * 0.9702;
    else if (mcChannelNumber == 364168.0)
        XSEC = 15.01E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 364169.0)
        XSEC = 1.2349E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 364170.0)
        XSEC = 19153.0E+03 * 0.82457 * 0.9702;
    else if (mcChannelNumber == 364171.0)
        XSEC = 19145.0E+03 * 0.13102 * 0.9702;
    else if (mcChannelNumber == 364172.0)
        XSEC = 19143.0E+03 * 0.044183 * 0.9702;
    else if (mcChannelNumber == 364173.0)
        XSEC = 945.69E+03 * 0.67481 * 0.9702;
    else if (mcChannelNumber == 364174.0)
        XSEC = 946.37E+03 * 0.24282 * 0.9702;
    else if (mcChannelNumber == 364175.0)
        XSEC = 945.63E+03 * 0.083353 * 0.9702;
    else if (mcChannelNumber == 364176.0)
        XSEC = 339.75E+03 * 0.59858 * 0.9702;
    else if (mcChannelNumber == 364177.0)
        XSEC = 339.80E+03 * 0.29252 * 0.9702;
    else if (mcChannelNumber == 364178.0)
        XSEC = 339.70E+03 * 0.11088 * 0.9702;
    else if (mcChannelNumber == 364179.0)
        XSEC = 72.077E+03 * 0.54829 * 0.9702;
    else if (mcChannelNumber == 364180.0)
        XSEC = 72.105E+03 * 0.32017 * 0.9702;
    else if (mcChannelNumber == 364181.0)
        XSEC = 72.077E+03 * 0.13865 * 0.9702;
    else if (mcChannelNumber == 364182.0)
        XSEC = 15.050E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 364183.0)
        XSEC = 1.2334E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 364184.0)
        XSEC = 19155.0E+03 * 0.82462 * 0.9702;
    else if (mcChannelNumber == 364185.0)
        XSEC = 19154.0E+03 * 0.12951 * 0.9702;
    else if (mcChannelNumber == 364186.0)
        XSEC = 19152.0E+03 * 0.045076 * 0.9702;
    else if (mcChannelNumber == 364187.0)
        XSEC = 945.58E+03 * 0.68329 * 0.9702;
    else if (mcChannelNumber == 364188.0)
        XSEC = 946.49E+03 * 0.24245 * 0.9702;
    else if (mcChannelNumber == 364189.0)
        XSEC = 945.87E+03 * 0.086159 * 0.9702;
    else if (mcChannelNumber == 364190.0)
        XSEC = 339.69E+03 * 0.59884 * 0.9702;
    else if (mcChannelNumber == 364191.0)
        XSEC = 339.84E+03 * 0.29032 * 0.9702;
    else if (mcChannelNumber == 364192.0)
        XSEC = 339.68E+03 * 0.11153 * 0.9702;
    else if (mcChannelNumber == 364193.0)
        XSEC = 72.078E+03 * 0.56172 * 0.9702;
    else if (mcChannelNumber == 364194.0)
        XSEC = 71.990E+03 * 0.31984 * 0.9702;
    else if (mcChannelNumber == 364195.0)
        XSEC = 71.944E+03 * 0.13604 * 0.9702;
    else if (mcChannelNumber == 364196.0)
        XSEC = 15.053E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 364197.0)
        XSEC = 1.2342E+03 * 1.0 * 0.9702;
    else if (mcChannelNumber == 361106.0)
        XSEC = 1.9011E+06 * 1.026;
    else if (mcChannelNumber == 361107.0)
        XSEC = 1.9011E+06 * 1.026;
    else if (mcChannelNumber == 361108.0)
        XSEC = 1.9011E+06 * 1.026;
    else if (mcChannelNumber == 410470.0)
        XSEC = 0.54383 * 831.76 * 1E+03;
    else if (mcChannelNumber == 410471.0)
        XSEC = 0.45627 * 1.1398 * 729.9 * 1E+03;
    else if (mcChannelNumber == 410472.0)
        XSEC = 0.10546 * 1.1398 * 729.9 * 1E+03;
    else if (mcChannelNumber == 410644.0)
        XSEC = 2.0267e+03 * 1.0170;
    else if (mcChannelNumber == 410645.0)
        XSEC = 1.2675e+03 * 1.0167;
    else if (mcChannelNumber == 410646.0)
        XSEC = 3.7937E+04 * 0.9450;
    else if (mcChannelNumber == 410647.0)
        XSEC = 3.7907E+04 * 0.9457;
    else if (mcChannelNumber == 410658.0)
        XSEC = 3.6993E+04 * 1.1935;
    else if (mcChannelNumber == 410659.0)
        XSEC = 2.2175E+04 * 1.1849;
    else if (mcChannelNumber == 364250.0)
        XSEC = 1252.23;
    else if (mcChannelNumber == 364253.0)
        XSEC = 4579.0;
    else if (mcChannelNumber == 364254.0)
        XSEC = 12501.;
    else if (mcChannelNumber == 364255.0)
        XSEC = 3234.4;
    else if (mcChannelNumber == 363355.0)
        XSEC = 0.28003 * 15561.;
    else if (mcChannelNumber == 363356.0)
        XSEC = 0.14158 * 15564.;
    else if (mcChannelNumber == 363357.0)
        XSEC = 6797.5;
    else if (mcChannelNumber == 363358.0)
        XSEC = 3433;
    else if (mcChannelNumber == 363359.0)
        XSEC = 24708.;
    else if (mcChannelNumber == 363360.0)
        XSEC = 24724.;
    else if (mcChannelNumber == 363489.0)
        XSEC = 11419.;
    else if (mcChannelNumber == 402970.0)
        XSEC = 1000 * 0.94588;
    else if (mcChannelNumber == 402975.0)
        XSEC = 1000 * 0.063932;
    else if (mcChannelNumber == 402985.0)
        XSEC = 1000 * 0.0023725;
    else if (mcChannelNumber == 402995.0)
        XSEC = 1000 * 0.9461 * 0.64072;
    else if (mcChannelNumber == 403000.0)
        XSEC = 1000 * 0.063918 * 0.6398;
    else if (mcChannelNumber == 403010.0)
        XSEC = 1000 * 0.0023733 * 0.64277;
    else if (mcChannelNumber == 403020.0)
        XSEC = 1000 * 1.8933 * 0.64181;
    else if (mcChannelNumber == 403025.0)
        XSEC = 1000 * 0.12785 * 0.64018;
    else if (mcChannelNumber == 403035.0)
        XSEC = 1000 * 0.004748 * 0.65019;
    else if (mcChannelNumber == 403022.0)
        XSEC = 1000 * 0.53705 * 0.64552;
    else if (mcChannelNumber == 402997.0)
        XSEC = 1000 * 0.26853 * 0.63999;
    else if (mcChannelNumber == 402972.0)
        XSEC = 1000 * 0.26848 * 1;
    else if (mcChannelNumber == 403005.0)
        XSEC = 1000 * 0.010363 * 0.64237;
    else if (mcChannelNumber == 402980.0)
        XSEC = 1000 * 0.010358 * 1;
    else if (mcChannelNumber == 403030.0)
        XSEC = 1000 * 0.02072 * 0.64646;
    else if (mcChannelNumber == 312428.0)
        XSEC = 1000 * 11.496;
    else if (mcChannelNumber == 312429.0)
        XSEC = 1000 * 0.77396;
    else if (mcChannelNumber == 312430.0)
        XSEC = 1000 * 0.03167;
    else if (mcChannelNumber == 312431.0)
        XSEC = 1000 * 11.48;
    else if (mcChannelNumber == 312432.0)
        XSEC = 1000 * 0.77257;
    else if (mcChannelNumber == 312433.0)
        XSEC = 1000 * 0.031615;
    else if (mcChannelNumber == 312434.0)
        XSEC = 1000 * 11.451;
    else if (mcChannelNumber == 312435.0)
        XSEC = 1000 * 0.7711;
    else if (mcChannelNumber == 312436.0)
        XSEC = 1000 * 0.031472;
    else if (mcChannelNumber == 312860.0)
        XSEC = 1000 * 3.2155;
    else if (mcChannelNumber == 312863.0)
        XSEC = 1000 * 0.13006;
    else if (mcChannelNumber == 312861.0)
        XSEC = 1000 * 0.12985;
    else if (mcChannelNumber == 312862.0)
        XSEC = 1000 * 3.2134;
    else if (mcChannelNumber == 312864.0)
        XSEC = 1000 * 3.2154;
    else if (mcChannelNumber == 312865.0)
        XSEC = 1000 * 0.13017;

    else
        (cout << "ERROR :: MC Channel Not Found!!!!!" << endl);
    return XSEC;
}

double NtupleMaker::CalLumNormSF(TChain *chain, double xSec) {
    //    TFile *file2 = new TFile(inFileName.c_str(),"READ");
    //    TTree *meta = (TTree *)file2->Get("metaTree");
    chain->SetBranchAddress("totalEventsWeighted", &(sumOfWeights));
    //    chain->SetBranchAddress("inputFileName", &(filename));
    vector<string> fileList;
    double Num = 0;
    for (Long64_t i = 0; i < chain->GetEntries(); i++) {
        chain->GetEntry(i);
        //        bool isDuplicated = false;
        //        for(auto na : fileList) {
        //            if(*(filename)==na) {
        //                isDuplicated = true;
        //                break;
        //            }
        //        }
        //        if(!isDuplicated) {
        //            fileList.push_back(*(filename));
        Num += (sumOfWeights);
        //            cout<<"bookkeeping "<<(filename)<<endl;
        //        }
    }
    cout << "lum: " << luminosity << endl;
    cout << "Xsec: " << xSec << endl;
    cout << "SOW: " << Num << endl;
    fileList.clear();
    //    delete meta;
    //    file2->Close();
    return luminosity * xSec / Num;
}

double NtupleMaker::CalSOW(TChain *chain) {
    //    TFile *file2 = new TFile(inFileName.c_str(),"READ");
    //    TTree *meta = (TTree *)file2->Get("metaTree");
    chain->SetBranchAddress("totalEventsWeighted", &(sumOfWeights));
    vector<string> fileList;
    double Num = 0;
    for (Long64_t i = 0; i < chain->GetEntries(); i++) {
        chain->GetEntry(i);
        //        bool isDuplicated = false;
        //        for(auto na : fileList) {
        //            if(*(filename)==na) {
        //                isDuplicated = true;
        //                break;
        //            }
        //        }
        //        if(!isDuplicated) {
        //            fileList.push_back(*(filename));
        Num += (sumOfWeights);
        //            cout<<"bookkeeping "<<(filename)<<endl;
        //        }
    }
    return Num;
}

void NtupleMaker::InitialVarible() {
    ele_pt = 0;
    ele_eta = 0;
    ele_phi = 0;
    //    isData = 0;
    ele_isTight = 0;
    weight = 0;
    mu_pt = 0;
    mu_eta = 0;
    mu_phi = 0;
    mu_isTight = 0;
    tau_pt = 0;
    tau_eta = 0;
    tau_phi = 0;
    tau_C = 0;
    mu_C = 0;
    ele_C = 0;
    tau_isTight = 0;
    tau_isRNNMEL = 0;
    tau_isRNNMEM = 0;
    tau_isRNNMET = 0;
    tau_isRNNLEM = 0;
    tau_isRNNTEM = 0;
    tau_isBDTLEM = 0;
    tau_isBDTMEM = 0;
    tau_isBDTTEM = 0;
    tauRNNMELSF = 1.0;
    tauRNNMEMSF = 1.0;
    tauRNNMETSF = 1.0;
    tauRNNLEMSF = 1.0;
    tauRNNTEMSF = 1.0;
    tauBDTLEMSF = 1.0;
    tauBDTMEMSF = 1.0;
    tauBDTTEMSF = 1.0;
    muonTrigSF = 1.0;
    muonRecoSF = 1.0;
    muonIsoSF = 1.0;
    muonTtvaSF = 1.0;
    electronTrigSF = 1.0;
    electronIDSF = 1.0;
    electronRecoSF = 1.0;
    electronIsoSF = 1.0;
    electronL1CaloSF = 1.0;
    tauRecoSF = 1.0;
    tauEleOlrSF = 1.0;
    tauEJetIDSF = 1.0;
    //    xsecSF = 0;
    //    lumSF = 0;
    //    NormSF = 0.0;
    Etag = -1;
    weightB77 = -1;
    weightB85 = -1;
    NTauLoose = 0;
    NTauTight = 0;
    Evtag = -1;
    EtagT1 = -1;
    EtagT2 = -1;
    jetJvtSF = 1.0;
    DPhi_ll = 0.0;
    IsCharge = 0;
    met = 0;
    met_phi = 0;
    njets = 0;
    nbjets = 0;
    nbjetsDL1r77 = 0;
    nbjetsDL1r85 = 0;
    emu = 0;
    etau = 0;
    mutau = 0;
    muonTrigSF = 1.0;
    muonRecoSF = 1.0;
    muonIsoSF = 1.0;
    muonTtvaSF = 1.0;
    electronTrigSF = 1.0;
    electronIDSF = 1.0;
    electronRecoSF = 1.0;
    electronIsoSF = 1.0;
    electronL1CaloSF = 1.0;
    tauRecoSF = 1.0;
    tauEleOlrSF = 1.0;
    tauEJetIDSF = 1.0;
    //    ele_d0sig=0;
    //    ele_dz0=0;
    //    mu_d0sig=0;
    //    mu_dz0=0;
    event_mT1 = 0;
    event_mT2 = 0;
    met_mT = 0;
    dRMETl1 = 0;
    dPhiMETl2 = 0;
    dPhiMETl1 = 0;
    dRMETl2 = 0;

    NTauLoose = 0;
    NTauTight = 0;
    Evtag = -1;
    EtagT1 = -1;
    EtagT2 = -1;
    jetJvtSF = 1.0;
    DPhi_ll = 0.0;
    IsCharge = 0;
    met = 0;
    met_phi = 0;
    met_eta = 0;
    njets = 0;
    nbjets = 0;
    Bjets_SF = 1;
    DPhi_ll = 0.0;
    M_ll = 0.0;
    DR_ll = 0.0;
    Pt_ll = 0.0;
    Eta_ll = 0.0;
    Phi_ll = 0.0;

    //    luminosity = 0;
}

void NtupleMaker::SkimProcessor(string inFileName, TChain *chain) {
    //    cout<<(wrkarea+inFileName+"_Skim.root").c_str()<<endl;
    //    TFile* ntupleF = new TFile((wrkarea+inFileName+"_Skim.root").c_str(),"recreate");
    TFile *ntupleF = new TFile((inFileName + "_Skim.root").c_str(), "recreate");
    EMuTauTree = new TTree("Emutau", "Emutau");
    EMuTauTree->SetDirectory(ntupleF);
    EMuTauTree->Branch("njets", &njets);
    EMuTauTree->Branch("nbjets", &nbjets);
    EMuTauTree->Branch("nbjetsDL1r77", &nbjetsDL1r77);
    EMuTauTree->Branch("nbjetsDL1r85", &nbjetsDL1r85);
    EMuTauTree->Branch("met", &met);
    EMuTauTree->Branch("met_phi", &met_phi);
    EMuTauTree->Branch("met_eta", &met_eta);
    EMuTauTree->Branch("ele_eta", &ele_eta);
    EMuTauTree->Branch("ele_pt", &ele_pt);
    EMuTauTree->Branch("ele_phi", &ele_phi);
    //    EMuTauTree->Branch("ele_d0sig",&ele_d0sig);
    //    EMuTauTree->Branch("ele_dz0",&ele_dz0);
    //    EMuTauTree->Branch("mu_d0sig",&mu_d0sig);
    //    EMuTauTree->Branch("mu_dz0",&mu_dz0);
    EMuTauTree->Branch("ele_isTight", &ele_isTight);
    EMuTauTree->Branch("ele_C", &ele_C);
    EMuTauTree->Branch("mu_pt", &mu_pt);
    EMuTauTree->Branch("mu_C", &mu_C);
    EMuTauTree->Branch("mu_eta", &mu_eta);
    EMuTauTree->Branch("mu_e", &mu_e);
    EMuTauTree->Branch("mu_phi", &mu_phi);
    EMuTauTree->Branch("mu_isTight", &mu_isTight);
    EMuTauTree->Branch("tau_pt", &tau_pt);
    EMuTauTree->Branch("tau_C", &tau_C);
    EMuTauTree->Branch("tau_eta", &tau_eta);
    EMuTauTree->Branch("tau_e", &tau_e);
    EMuTauTree->Branch("tau_phi", &tau_phi);
    EMuTauTree->Branch("tau_isTight", &tau_isTight);
    EMuTauTree->Branch("isData", &isData);
    EMuTauTree->Branch("NormSF", &NormSF);
    EMuTauTree->Branch("SumofWeight", &SumofWeight);
    EMuTauTree->Branch("weight", &weight);
    EMuTauTree->Branch("weightB77", &weightB77);
    EMuTauTree->Branch("weightB85", &weightB85);
    EMuTauTree->Branch("Etag", &Etag);
    EMuTauTree->Branch("Evtag", &Evtag);
    EMuTauTree->Branch("EtagT2", &EtagT2);
    EMuTauTree->Branch("EtagT1", &EtagT1);
    EMuTauTree->Branch("NTauLoose", &NTauLoose);
    EMuTauTree->Branch("NTauTight", &NTauTight);
    EMuTauTree->Branch("DPhi_ll", &DPhi_ll);
    EMuTauTree->Branch("IsCharge", &IsCharge);
    EMuTauTree->Branch("DR_ll", &DR_ll);
    EMuTauTree->Branch("M_ll", &M_ll);
    EMuTauTree->Branch("Pt_ll", &Pt_ll);
    EMuTauTree->Branch("Eta_ll", &Eta_ll);
    EMuTauTree->Branch("Phi_ll", &Phi_ll);

    EMuTauTree->Branch("emu", &emu);
    EMuTauTree->Branch("etau", &etau);
    EMuTauTree->Branch("mutau", &mutau);
    EMuTauTree->Branch("NTauLoose", &NTauLoose);
    EMuTauTree->Branch("NTauTight", &NTauTight);
    EMuTauTree->Branch("DPhi_ll", &DPhi_ll);
    EMuTauTree->Branch("IsCharge", &IsCharge);
    EMuTauTree->Branch("tau_isRNNMEL", &tau_isRNNMEL);
    EMuTauTree->Branch("tau_isRNNMEM", &tau_isRNNMEM);
    EMuTauTree->Branch("tau_isRNNMET", &tau_isRNNMET);
    EMuTauTree->Branch("tau_isRNNLEM", &tau_isRNNLEM);
    EMuTauTree->Branch("tau_isRNNTEM", &tau_isRNNTEM);
    EMuTauTree->Branch("tau_isBDTLEM", &tau_isBDTLEM);
    EMuTauTree->Branch("tau_isBDTMEM", &tau_isBDTMEM);
    EMuTauTree->Branch("tau_isBDTTEM", &tau_isBDTTEM);
    EMuTauTree->Branch("event_mT1", &event_mT1);
    EMuTauTree->Branch("event_mT2", &event_mT2);
    EMuTauTree->Branch("met_mT", &met_mT);
    EMuTauTree->Branch("dRMETl1", &dRMETl1);
    EMuTauTree->Branch("dPhiMETl2", &dPhiMETl2);
    EMuTauTree->Branch("dPhiMETl1", &dPhiMETl1);
    EMuTauTree->Branch("dRMETl2", &dRMETl2);

    //    EMuTauTree->Branch("tau_isRNNMEL",&tau_isRNNMEL);
    //    EMuTauTree->Branch("tau_isRNNMEM",&tau_isRNNMEM);
    //    EMuTauTree->Branch("tau_isRNNMET",&tau_isRNNMET);
    //    EMuTauTree->Branch("tau_isRNNLEM",&tau_isRNNLEM);
    //    EMuTauTree->Branch("tau_isRNNTEM",&tau_isRNNTEM);
    //    EMuTauTree->Branch("tau_isBDTLEM",&tau_isBDTLEM);
    //    EMuTauTree->Branch("tau_isBDTMEM",&tau_isBDTMEM);
    //    EMuTauTree->Branch("tau_isBDTTEM",&tau_isBDTTEM);
    //    EMuTauTree->Branch("tauRNNMELSF",&tauRNNMELSF);
    //    EMuTauTree->Branch("tauRNNMEMSF",&tauRNNMEMSF);
    //    EMuTauTree->Branch("tauRNNMETSF",&tauRNNMETSF);
    //    EMuTauTree->Branch("tauRNNLEMSF",&tauRNNLEMSF);
    //    EMuTauTree->Branch("tauRNNTEMSF",&tauRNNTEMSF);
    //    EMuTauTree->Branch("tauBDTLEMSF",&tauBDTLEMSF);
    //    EMuTauTree->Branch("tauBDTMEMSF",&tauBDTMEMSF);
    //    EMuTauTree->Branch("tauBDTTEMSF",&tauBDTTEMSF);

    cout << chain->GetEntries() << endl;

    int ElectronTight;
    int ElectronLoose;
    int MuonTight;
    int MuonLoose;
    int TauTight;
    int TauLoose;
    int cnt0 = 0;
    bool ETT = 0;
    bool MTT = 0;
    int cnt1;

    for (int ii = 0; ii < chain->GetEntries(); ii++) {
        chain->GetEntry(ii);
        InitialVarible();

        if (ii == 0) {
            if (isData) {
                CalNMSF = 1;
                CalSFSOW = 1;
            } else {
                double XSection = FindXsec(mcChannelNumber);
                CalNMSF = CalLumNormSF(meta, XSection);
                CalSFSOW = CalSOW(meta);
                //                CalNMSF = CalLumNormSF(mcChannelNumber);
                cout << "NormSF: " << CalNMSF << endl;
            }
        }
        if (!((HLT_mu50) || HLT_mu26_ivarmedium || HLT_e140_lhloose_nod0 || HLT_e26_lhtight_nod0_ivarloose ||
              HLT_e120_lhloose || HLT_mu20_iloose_L1MU15 || HLT_e24_lhmedium_L1EM20VH || HLT_e60_lhmedium ||
              HLT_e60_lhmedium_nod0))
            continue;
        if (!(el_trigMatch_HLT_e60_lhmedium_nod0 || el_trigMatch_HLT_e60_lhmedium ||
              el_trigMatch_HLT_e24_lhmedium_L1EM20VH || el_trigMatch_HLT_e120_lhloose ||
              el_trigMatch_HLT_e26_lhtight_nod0_ivarloose || el_trigMatch_HLT_e140_lhloose_nod0 ||
              mu_trigMatch_HLT_mu50 || mu_trigMatch_HLT_mu20_iloose_L1MU15 || mu_trigMatch_HLT_mu26_ivarmedium))
            continue;
        //        if( Ele_TriggerMatched == false && Mu_TriggerMatched == false ) continue;
        //        //if( EventTag > 2 ) continue;
        //
        //        cnt0++;
        ////        if(fabs(dPhi_ll) < 2.7) continue;
        //
        weight = EventWeight;
        xsecSF = xsec;
        NormSF = CalNMSF;
        SumofWeight = CalSFSOW;
        //
        ElectronTight = 0;
        ElectronLoose = 0;
        MuonTight = 0;
        MuonLoose = 0;
        TauTight = 0;
        TauLoose = 0;
        //
        //
        ////        cnt1=0;
        ////        ETT=0;
        //        MTT=0;
        //
        int EC = 0;
        int MC = 0;
        int TC = 0;

        for (size_t jj = 0; jj < (Ele_eta)->size(); jj++) {
            if (Ele_pt->at(jj) < 65000.0) continue;
            //                if( fabs(Ele_eta->at(jj)) > 2.47 || (  fabs(Ele_eta->at(jj)) > 1.37 &&
            //                fabs(Ele_eta->at(jj)) < 1.52 ) ) continue;
            if (fabs(el_delta_z0_sintheta->at(jj)) > 0.5 || fabs(el_d0sig->at(jj)) > 5.0) continue;
            if (el_isElMedium->at(jj) != 1.0) continue;

            ElectronLoose++;
            if (!(((el_isElTight->at(jj)) && (el_isolation_FixedCutTight->at(jj))))) continue;
            ele_pt = Ele_pt->at(jj) * 0.001;
            ele_eta = (*Ele_eta)[jj];
            // cout<<ele_eta<<endl;
            // cout<<" " <<endl;
            ele_phi = (*Ele_phi)[jj];
            EC = (*el_charge)[jj];
            ele_C = (*el_charge)[jj];
            //	    if (!isData){
            //            electronL1CaloSF = (*Ele_L1CaloSF)[jj];
            //            electronIDSF = (*Ele_IDSF)[jj];
            //            electronIsoSF = (*Ele_IsoSF)[jj];
            //            electronRecoSF = (*Ele_RecoSF)[jj];
            //            electronTrigSF = (*Ele_TrigEff)[jj];
            //	    }
            ElectronTight++;
            ele_isTight = 1;
            //// if (((((*Ele_ID_Tight)[jj] == 1)&&((*Ele_Iso)[jj] == 1))))
        }
        //
        for (size_t kk = 0; kk < (Mu_pt)->size(); kk++) {
            if (Mu_pt->at(kk) < 65000.0) continue;
            //          if( fabs(Mu_eta->at(kk)) > 2.5 ) continue;
            if (!mu_isHighPt->at(kk)) continue;
            if (fabs(mu_delta_z0_sintheta->at(kk)) > 0.5 || fabs(mu_d0sig->at(kk)) > 3.0) continue;
            MuonLoose++;
            if (!mu_isolation_FixedCutLoose->at(kk)) continue;
            mu_pt = (*Mu_pt)[kk] * 0.001;
            mu_eta = (*Mu_eta)[kk];
            mu_phi = (*Mu_phi)[kk];
            MC = (*mu_charge)[kk];
            mu_C = (*mu_charge)[kk];
            //	    if (!isData){
            //            muonRecoSF = ((*Mu_RecoSF)[kk]);
            //            muonIsoSF = ((*Mu_IsoSF)[kk]);
            //            muonTtvaSF = ((*Mu_TrackSF)[kk]);
            //            muonTrigSF = ((*Mu_TrigSF)[kk]);
            //	    }
            MuonTight++;
            mu_isTight = 1;
        }
        //
        for (size_t ll = 0; ll < (Tau_pt)->size(); ll++) {
            if (Tau_pt->at(ll) < 65000.0) continue;
            //              if( fabs(Tau_eta->at(ll)) > 2.47 || (  fabs(Tau_eta->at(ll)) > 1.37 && fabs(Tau_eta->at(ll))
            //              < 1.52 ) ) continue;
            if (fabs(tau_charge->at(ll)) != 1.0) continue;
            if (tau_nTracks->at(ll) != 1.0 && tau_nTracks->at(ll) != 3.0) continue;

            TauLoose++;

            if (tau_isRNNMedium->at(ll) != 1.0) continue;
            tau_pt = (*Tau_pt)[ll] * 0.001;
            tau_eta = (*Tau_eta)[ll];
            tau_phi = (*Tau_phi)[ll];
            TC = (*tau_charge)[ll];
            tau_C = (*tau_charge)[ll];
            TauTight++;
            tau_isTight = 1;
        }
        //        Evtag = EventTag;
        NTauTight = TauTight;
        NTauLoose = TauLoose;
        if ((TauTight == 0) && (MuonLoose == 1) && (ElectronLoose == 1)) Etag = 0;
        if ((TauTight == 1) && (MuonTight == 0) && (ElectronTight == 1)) Etag = 1;
        if ((TauTight == 1) && (MuonTight == 1) && (ElectronTight == 0)) Etag = 2;
        if ((TauLoose > 0) && (MuonTight == 0) && (ElectronTight == 1)) EtagT1 = 3;
        if ((TauLoose > 0) && (MuonTight == 1) && (ElectronTight == 0)) EtagT1 = 4;
        if (TauLoose > 0) EtagT2 = 5;
        //
        met = MET_met * 0.001;
        met_phi = MET_phi;
        //        met_eta = 0;
        //
        //
        int NBJ = 0;

        njets = (jet_pt)->size();
        for (size_t mm = 0; mm < (jet_pt)->size(); mm++) {
            //       cout << (int)(jet_isbtagged_DL1r_77->at(mm))<<endl;
            //               if( jet_pt->at(mm) < 20000.0 ) continue;
            //               if( fabs(jet_eta->at(mm)) > 2.5 ) continue;
            if ((int)(jet_isbtagged_DL1r_77->at(mm)) > 0) {
                nbjetsDL1r77++;
            }
            if ((int)(jet_isbtagged_DL1r_85->at(mm)) > 0) {
                nbjetsDL1r85++;
            }
            // Check Jet Cleaning
            //               if( jet_pt->at(mm)*0.001 < 60.0 && fabs(jet_eta->at(mm)) <  2.4 && jet_jvt->at(mm) <= 0.2
            //               ) continue; if( jet_pt->at(mm)*0.001 < 60.0 && fabs(jet_eta->at(mm)) >= 2.4 ) continue; if(
            //               jet_mv2c10->at(mm) >  0.07){ nbjets++;} if( jet_DL1r->at(mm) >  2.2){ nbjetsDL1r77++;} if(
            //               jet_DL1r->at(mm) >  1.27){ nbjetsDL1r85++;}
        }

        if (isData) {
            weight = 1;
            weightB77 = 1;
            weightB85 = 1;
        } else {
            weightB77 = weight_bTagSF_DL1r_77;
            weightB85 = weight_bTagSF_DL1r_85;
            if (Etag == 0) weight = weight_mc * weight_pileup * weight_leptonSF * NormSF * weight_jvt;
            if (Etag == 1) weight = weight_mc * weight_pileup * weight_leptonSF * weight_tauSF * NormSF * weight_jvt;
            if (Etag == 2) weight = weight_mc * weight_pileup * weight_leptonSF * weight_tauSF * NormSF * weight_jvt;
            //            if( EtagT1 == 3) weight =
            //            PrwWeight*MCWeight*electronTrigSF*electronIDSF*electronRecoSF*electronIsoSF*jetJvtSF; if(
            //            EtagT1 == 4) weight = PrwWeight*MCWeight*muonTrigSF*muonRecoSF*muonIsoSF*muonTtvaSF*jetJvtSF;
        }
        //
        //
        int ChaT = 0;
        //        TLorentzVector FMET(1,1,1,1);
        TLorentzVector IMET(1, 1, 1, 1);

        if (Etag == 0) {
            ChaT = EC * MC;
            //            cout << ChaT <<endl;
            DPhi_ll = CaldPhi(ele_phi, mu_phi);
            DR_ll = sqrt((ele_eta - mu_eta) * (ele_eta - mu_eta) + DPhi_ll * DPhi_ll);
            emu = 1;
            mutau = 0;
            etau = 0;

            //            met = Event_met;
            //            met_phi = Event_met_Phi;
        } else if (Etag == 1) {
            ChaT = EC * TC;
            DPhi_ll = CaldPhi(ele_phi, tau_phi);
            DR_ll = sqrt((ele_eta - tau_eta) * (ele_eta - tau_eta) + DPhi_ll * DPhi_ll);
            emu = 0;
            mutau = 0;
            etau = 1;

            //            FMET.SetPtEtaPhiM(Event_met,tau_eta,Event_met_Phi,0.0);
            //            met = FMET.Pt();
            //            met_phi = FMET.Phi();
        } else if (Etag == 2) {
            ChaT = TC * MC;
            DPhi_ll = CaldPhi(mu_phi, tau_phi);
            DR_ll = sqrt((mu_eta - tau_eta) * (mu_eta - tau_eta) + DPhi_ll * DPhi_ll);
            emu = 0;
            mutau = 1;
            etau = 0;

            //            FMET.SetPtEtaPhiM(Event_met,tau_eta,Event_met_Phi,0.0);
            //            met = FMET.Pt();
            //            met_phi = FMET.Phi();
        }

        IsCharge = ChaT;

        TLorentzVector lp1(1, 1, 1, 1);
        TLorentzVector lp2(1, 1, 1, 1);
        if (Etag == 0) {
            lp1.SetPtEtaPhiM(ele_pt, ele_eta, ele_phi, ElePDGMass);
            lp2.SetPtEtaPhiM(mu_pt, mu_eta, mu_phi, MuonPDGMass);
            ele_e = lp1.E();
            mu_e = lp2.E();
            M_ll = (lp1 + lp2).M();
            //    IMET.SetPtEtaPhiM(Event_met,Event_met_Eta,Event_met_Phi,Event_met_M);
            event_mT1 = 0;
            event_mT2 = 0;
            dRMETl1 = 0;
            dPhiMETl1 = 0;
            dRMETl2 = 0;
            dPhiMETl2 = 0;
            //    event_mT1 =
            //    sqrt((sqrt(lp1.E()*lp1.E()-lp1.Pz()*lp1.Pz())+IMET.E())*(sqrt(lp1.E()*lp1.E()-lp1.Pz()*lp1.Pz())+IMET.E())-(lp1.Px()+IMET.Px())*(lp1.Px()+IMET.Px())-(lp1.Py()+IMET.Py())*(lp1.Py()+IMET.Py()));
            //    event_mT2 =
            //    sqrt((sqrt(lp2.E()*lp2.E()-lp2.Pz()*lp2.Pz())+IMET.E())*(sqrt(lp2.E()*lp2.E()-lp2.Pz()*lp2.Pz())+IMET.E())-(lp2.Px()+IMET.Px())*(lp2.Px()+IMET.Px())-(lp2.Py()+IMET.Py())*(lp2.Py()+IMET.Py()));
            //    dRMETl1 = IMET.DeltaR(lp1);
            //    dPhiMETl1 = IMET.DeltaPhi(lp1);
            //    dRMETl2 = IMET.DeltaR(lp2);
            //    dPhiMETl2 = IMET.DeltaPhi(lp2);

        } else if (Etag == 1) {
            lp1.SetPtEtaPhiM(ele_pt, ele_eta, ele_phi, ElePDGMass);
            lp2.SetPtEtaPhiM(tau_pt, tau_eta, tau_phi, TauPDGMass);
            IMET.SetPtEtaPhiM(met, tau_eta, met_phi, 0);
            ele_e = lp1.E();
            tau_e = lp2.E();
            M_ll = (lp1 + lp2 + IMET).M();
            //    IMET.SetPtEtaPhiM(Event_met,Event_met_Eta,Event_met_Phi,Event_met_M);
            event_mT1 =
                sqrt((sqrt(lp1.E() * lp1.E() - lp1.Pz() * lp1.Pz()) + IMET.E()) *
                         (sqrt(lp1.E() * lp1.E() - lp1.Pz() * lp1.Pz()) + IMET.E()) -
                     (lp1.Px() + IMET.Px()) * (lp1.Px() + IMET.Px()) - (lp1.Py() + IMET.Py()) * (lp1.Py() + IMET.Py()));
            event_mT2 =
                sqrt((sqrt(lp2.E() * lp2.E() - lp2.Pz() * lp2.Pz()) + IMET.E()) *
                         (sqrt(lp2.E() * lp2.E() - lp2.Pz() * lp2.Pz()) + IMET.E()) -
                     (lp2.Px() + IMET.Px()) * (lp2.Px() + IMET.Px()) - (lp2.Py() + IMET.Py()) * (lp2.Py() + IMET.Py()));
            dRMETl1 = IMET.DeltaR(lp1);
            dPhiMETl1 = IMET.DeltaPhi(lp1);
            dRMETl2 = IMET.DeltaR(lp2);
            dPhiMETl2 = IMET.DeltaPhi(lp2);
            met_mT = IMET.M();
        } else if (Etag == 2) {
            lp1.SetPtEtaPhiM(mu_pt, mu_eta, mu_phi, MuonPDGMass);
            lp2.SetPtEtaPhiM(tau_pt, tau_eta, tau_phi, TauPDGMass);
            IMET.SetPtEtaPhiM(met, tau_eta, met_phi, 0);
            mu_e = lp1.E();
            tau_e = lp2.E();
            M_ll = (lp1 + lp2 + IMET).M();
            //    IMET.SetPtEtaPhiM(Event_met,Event_met_Eta,Event_met_Phi,Event_met_M);
            event_mT1 =
                sqrt((sqrt(lp1.E() * lp1.E() - lp1.Pz() * lp1.Pz()) + IMET.E()) *
                         (sqrt(lp1.E() * lp1.E() - lp1.Pz() * lp1.Pz()) + IMET.E()) -
                     (lp1.Px() + IMET.Px()) * (lp1.Px() + IMET.Px()) - (lp1.Py() + IMET.Py()) * (lp1.Py() + IMET.Py()));
            event_mT2 =
                sqrt((sqrt(lp2.E() * lp2.E() - lp2.Pz() * lp2.Pz()) + IMET.E()) *
                         (sqrt(lp2.E() * lp2.E() - lp2.Pz() * lp2.Pz()) + IMET.E()) -
                     (lp2.Px() + IMET.Px()) * (lp2.Px() + IMET.Px()) - (lp2.Py() + IMET.Py()) * (lp2.Py() + IMET.Py()));
            dRMETl1 = IMET.DeltaR(lp1);
            dPhiMETl1 = IMET.DeltaPhi(lp1);
            dRMETl2 = IMET.DeltaR(lp2);
            dPhiMETl2 = IMET.DeltaPhi(lp2);
            met_mT = IMET.M();
        }
        Eta_ll = (lp1 + lp2).Eta();
        Phi_ll = (lp1 + lp2).Phi();
        Pt_ll = (lp1 + lp2).Pt();
        if ((ChaT) > 0) continue;
        if (fabs(DPhi_ll) < 2.7) continue;

        //        if(fabs(DPhi_ll-dPhi_ll) > 0.001 )
        //{
        //   cout <<"////////"<<(DPhi_ll-dPhi_ll)<<"////////"<<endl;
        //   cout << Etag << endl;
        //   cout << "Phi1= " <<dPhi_ll<<endl;
        //   cout << "Phi2= " <<DPhi_ll<<endl;
        //   cout << "cnt= " <<cnt1<<endl;
        //   cout << "ETT= " <<ETT<<endl;
        //   cout << "MTT= " <<MTT<<endl;
        //}
        //       if((ChaT) >0) continue;
        //       if(fabs(DPhi_ll) < 2.7) continue;
        //       njets= N_jets;
        //        cout << DPhi_ll <<endl;

        EMuTauTree->Fill();
    }

    cout << "     " << endl;
    cout << cnt0 << endl;
    //   cout << cnt1 << endl;

    ntupleF->cd();
    EMuTauTree->Write();
    ntupleF->Close();
    //   delete ntupleF;
    //   delete EMuTauTree;
}

void NtupleMaker::RunSkim() {
    TChain *ssTree = new TChain("nominal");
    meta = new TChain("sumWeights");
    typedef std::vector<std::string>::iterator STRING_ITOR;
    STRING_ITOR inF;
    string INFName;
    for (inF = InputFileList.begin(); inF != InputFileList.end(); ++inF) {
        cout << *inF << endl;
        INFName = *inF;
        ssTree->Add((*inF).c_str());
        meta->Add((*inF).c_str());
    }
    luminosity = Lum(INFName);
    cout << "lum" << luminosity << endl;
    cout << "mcCA" << mcChannelNumber << endl;
    cout << OutPutName << endl;
    ReadTreeLFVO(ssTree);

    SkimProcessor(OutPutName, ssTree);
    delete ssTree;
    delete meta;
}
