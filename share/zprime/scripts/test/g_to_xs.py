import numpy as np
import matplotlib.pyplot as plt

para_51 = [
    0.0023224160441653713,
    0.0548259786981602,
    -0.020176464093835427,
    0.0044964723204448526,
    -0.00048341538776611675,
    1.9714058629911877e-05,
]

f_xs_to_g_51 = np.poly1d(para_51[::-1])
x = range(8)
f_g_to_xs_51 = np.poly1d(np.polyfit(f_xs_to_g_51(x), x, 3))

print("#", f_xs_to_g_51(6))
print("#", f_g_to_xs_51(0.1))

x = np.linspace(0, 0.2, 100)
y = f_g_to_xs_51(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("g_to_xs_51.png")

print("scale 51:", f_g_to_xs_51(0.1) / f_g_to_xs_51(0.12))



para_69 =  [
            0.007437009700996319,
            0.13871544818408635,
            -0.03256666852093385,
            0.004587420176565141,
            -0.0003113237247549025,
            7.997652032141912e-06,
        ]

f_xs_to_g_69 = np.poly1d(para_69[::-1])
x = range(13)
f_g_to_xs_69 = np.poly1d(np.polyfit(f_xs_to_g_69(x), x, 3))

print("#", f_xs_to_g_69(12.5))
print("#", f_g_to_xs_69(0.46))

x = np.linspace(0, 0.5, 100)
y = f_g_to_xs_69(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("g_to_xs_69.png")

print("scale 69:", f_g_to_xs_69(0.1) / f_g_to_xs_69(0.12))