#!/usr/bin/env python3.10
import tkinter as tk1
import sqlite3 as sql
from PIL import ImageTk, Image

# Accessing Database
sql = sql.connect("data.db")
sql = sql.cursor()

# Creating the Table Window
tk = tk1.Tk()
tk.title("Modern Periodic Table")
tk.geometry("1622x950")
tk.resizable(0, 0)

# Setting up Image
img = ImageTk.PhotoImage(Image.open("Elements2.jpg"))
image = tk1.Label(tk, image=img)
image.pack()


# Button Function
def display_button_data(atomic_number, color):
    sql.execute("Select * From data Where AtomicNumber = {}".format(atomic_number))
    element_data = sql.fetchall()

    tk2 = tk1.Tk()
    tk2.title(element_data[0][1])
    tk2.geometry("360x330")
    tk2.resizable(0, 0)
    tk2.configure(bg=color)

    # Contents
    l1 = tk1.Label(tk2, text="Element : {}".format(element_data[0][1]), bg=color, font=('Chilanka', 20))
    l1.place(x=20, y=50)
    l2 = tk1.Label(tk2, text="Symbol : {}".format(element_data[0][2]), bg=color, font=('Chilanka', 20))
    l2.place(x=20, y=110)
    l3 = tk1.Label(tk2, text="Atomic Number : {}".format(element_data[0][0]), bg=color, font=('Chilanka', 20))
    l3.place(x=20, y=170)
    l4 = tk1.Label(tk2, text="Atomic Mass : {} amu".format(element_data[0][3]), bg=color, font=('Chilanka', 20))
    l4.place(x=20, y=230)

    tk2.mainloop()


# Contents of Table


# Group I
e1 = tk1.Button(tk, text="H\n1", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                command=lambda: display_button_data(1, "lemon chiffon"))
e1.place(x=50, y=140)
e3 = tk1.Button(tk, text="Li\n3", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                command=lambda: display_button_data(3, "light salmon"))
e3.place(x=50, y=210)
e11 = tk1.Button(tk, text="Na\n11", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                 command=lambda: display_button_data(11, "light salmon"))
e11.place(x=50, y=280)
e19 = tk1.Button(tk, text="K\n19", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                 command=lambda: display_button_data(19, "light salmon"))
e19.place(x=50, y=350)
e37 = tk1.Button(tk, text="Rb\n37", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                 command=lambda: display_button_data(37, "light salmon"))
e37.place(x=50, y=420)
e55 = tk1.Button(tk, text="Cs\n55", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                 command=lambda: display_button_data(55, "light salmon"))
e55.place(x=50, y=490)
e87 = tk1.Button(tk, text="Fr\n87", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="light salmon",
                 command=lambda: display_button_data(87, "light salmon"))
e87.place(x=50, y=560)

# Group II
e4 = tk1.Button(tk, text="Be\n4", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                command=lambda: display_button_data(4, "slateBlue1"))
e4.place(x=140, y=210)
e12 = tk1.Button(tk, text="Mg\n12", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                 command=lambda: display_button_data(12, "slateBlue1"))
e12.place(x=140, y=280)
e20 = tk1.Button(tk, text="Ca\n20", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                 command=lambda: display_button_data(20, "slateBlue1"))
e20.place(x=140, y=350)
e38 = tk1.Button(tk, text="Sr\n38", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                 command=lambda: display_button_data(38, "slateBlue1"))
e38.place(x=140, y=420)
e56 = tk1.Button(tk, text="Ba\n56", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                 command=lambda: display_button_data(56, "slateBlue1"))
e56.place(x=140, y=490)
e88 = tk1.Button(tk, text="Ra\n88", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="slateBlue1",
                 command=lambda: display_button_data(88, "slateBlue1"))
e88.place(x=140, y=560)

# Group III
e21 = tk1.Button(tk, text="Sc\n21", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(21, "SteelBlue1"))
e21.place(x=230, y=350)
e39 = tk1.Button(tk, text="Y\n39", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(39, "SteelBlue1"))
e39.place(x=230, y=420)
e71 = tk1.Button(tk, text="Lu\n71", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(771, "Skyblue1"))
e71.place(x=230, y=490)
e103 = tk1.Button(tk, text="Lr\n103", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                  command=lambda: display_button_data(103, "Skyblue1"))
e103.place(x=230, y=560)

# Group IV
e22 = tk1.Button(tk, text="Ti\n22", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(22, "SteelBlue1"))
e22.place(x=320, y=350)
e40 = tk1.Button(tk, text="Zr\n40", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(40, "SteelBlue1"))
e40.place(x=320, y=420)
e72 = tk1.Button(tk, text="Hf\n72", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(72, "SteelBlue1"))
e72.place(x=320, y=490)
e104 = tk1.Button(tk, text="Rf\n104", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(104, "SteelBlue1"))
e104.place(x=320, y=560)

# Group V
e23 = tk1.Button(tk, text="V\n23", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(23, "SteelBlue1"))
e23.place(x=410, y=350)
e41 = tk1.Button(tk, text="Nb\n41", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(441, "SteelBlue1"))
e41.place(x=410, y=420)
e73 = tk1.Button(tk, text="Ta\n73", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(73, "SteelBlue1"))
e73.place(x=410, y=490)
e105 = tk1.Button(tk, text="Db\n105", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(105, "SteelBlue1"))
e105.place(x=410, y=560)

# Group VI
e24 = tk1.Button(tk, text="Cr\n24", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(24, "SteelBlue1"))
e24.place(x=410, y=350)
e42 = tk1.Button(tk, text="Mo\n42", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(42, "SteelBlue1"))
e42.place(x=410, y=420)
e74 = tk1.Button(tk, text="W\n74", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(74, "SteelBlue1"))
e74.place(x=410, y=490)
e106 = tk1.Button(tk, text="Sg\n106", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(106, "SteelBlue1"))
e106.place(x=410, y=560)

# Group VII
e25 = tk1.Button(tk, text="Mn\n25", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(25, "SteelBlue1"))
e25.place(x=500, y=350)
e43 = tk1.Button(tk, text="Tc\n43", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(43, "SteelBlue1"))
e43.place(x=500, y=420)
e75 = tk1.Button(tk, text="Re\n75", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(75, "SteelBlue1"))
e75.place(x=500, y=490)
e107 = tk1.Button(tk, text="Bh\n107", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(107, "SteelBlue1"))
e107.place(x=500, y=560)

# Group VIII
e26 = tk1.Button(tk, text="Fe\n26", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(26, "SteelBlue1"))
e26.place(x=590, y=350)
e44 = tk1.Button(tk, text="Ru\n44", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(44, "SteelBlue1"))
e44.place(x=590, y=420)
e76 = tk1.Button(tk, text="Os\n76", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(76, "SteelBlue1"))
e76.place(x=590, y=490)
e108 = tk1.Button(tk, text="Hs\n108", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(108, "SteelBlue1"))
e108.place(x=590, y=560)

# Group IX
e27 = tk1.Button(tk, text="Co\n27", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(27, "SteelBlue1"))
e27.place(x=680, y=350)
e45 = tk1.Button(tk, text="Rh\n45", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(45, "SteelBlue1"))
e45.place(x=680, y=420)
e77 = tk1.Button(tk, text="Ir\n77", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(77, "SteelBlue1"))
e77.place(x=680, y=490)
e109 = tk1.Button(tk, text="Mt\n109", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(109, "SteelBlue1"))
e109.place(x=680, y=560)

# Group X
e28 = tk1.Button(tk, text="Ni\n28", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(28, "SteelBlue1"))
e28.place(x=770, y=350)
e46 = tk1.Button(tk, text="Pd\n46", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(46, "SteelBlue1"))
e46.place(x=770, y=420)
e78 = tk1.Button(tk, text="Pt\n78", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(78, "SteelBlue1"))
e78.place(x=770, y=490)
e110 = tk1.Button(tk, text="Ds \n110", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(110, "SteelBlue1"))
e110.place(x=770, y=560)

# Group XI
e29 = tk1.Button(tk, text="Cu\n29", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(29, "SteelBlue1"))
e29.place(x=860, y=350)
e47 = tk1.Button(tk, text="Ag\n47", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(47, "SteelBlue1"))
e47.place(x=860, y=420)
e79 = tk1.Button(tk, text="Au\n79", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(79, "SteelBlue1"))
e79.place(x=860, y=490)
e111 = tk1.Button(tk, text="Rg \n111", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(111, "SteelBlue1"))
e111.place(x=860, y=560)

# Group XII
e30 = tk1.Button(tk, text="Zn\n30", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(30, "SteelBlue1"))
e30.place(x=950, y=350)
e48 = tk1.Button(tk, text="Cd\n48", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(49, "SteelBlue1"))
e48.place(x=950, y=420)
e80 = tk1.Button(tk, text="Hg\n80", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                 command=lambda: display_button_data(80, "SteelBlue1"))
e80.place(x=950, y=490)
e112 = tk1.Button(tk, text="Cn \n112", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="SteelBlue1",
                  command=lambda: display_button_data(112, "SteelBlue1"))
e112.place(x=950, y=560)

# Group XIII
e5 = tk1.Button(tk, text="B\n5", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="medium spring green",
                command=lambda: display_button_data(5, "medium spring green"))
e5.place(x=1040, y=210)
e13 = tk1.Button(tk, text="Al\n13", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(13, "spring green"))
e13.place(x=1040, y=280)
e31 = tk1.Button(tk, text="Ga\n31", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(31, "spring green"))
e31.place(x=1040, y=350)
e49 = tk1.Button(tk, text="In\n49", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(49, "spring green"))
e49.place(x=1040, y=420)
e81 = tk1.Button(tk, text="Tl\n81", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(81, "spring green"))
e81.place(x=1040, y=490)
e113 = tk1.Button(tk, text="Nh\n113", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                  command=lambda: display_button_data(113, "spring green"))
e113.place(x=1040, y=560)

# Group XIV
e6 = tk1.Button(tk, text="C\n6", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                command=lambda: display_button_data(6, "lemon chiffon"))
e6.place(x=1130, y=210)
e14 = tk1.Button(tk, text="Si\n14", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(14, "medium spring green"))
e14.place(x=1130, y=280)
e32 = tk1.Button(tk, text="Ge\n32", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(32, "medium spring green"))
e32.place(x=1130, y=350)
e50 = tk1.Button(tk, text="Sn\n50", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(50, "spring green"))
e50.place(x=1130, y=420)
e82 = tk1.Button(tk, text="Pb\n82", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(82, "spring green"))
e82.place(x=1130, y=490)
e114 = tk1.Button(tk, text="Fl\n114", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                  command=lambda: display_button_data(114, "spring green"))
e114.place(x=1130, y=560)

# Group XV
e7 = tk1.Button(tk, text="N\n7", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                command=lambda: display_button_data(7, "lemon chiffon"))
e7.place(x=1220, y=210)
e15 = tk1.Button(tk, text="P\n15", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                 command=lambda: display_button_data(15, "lemon chiffon"))
e15.place(x=1220, y=280)
e33 = tk1.Button(tk, text="As\n33", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(33, "medium spring green"))
e33.place(x=1220, y=350)
e51 = tk1.Button(tk, text="Sb\n51", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(51, "medium spring green"))
e51.place(x=1220, y=420)
e83 = tk1.Button(tk, text="Bi\n83", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                 command=lambda: display_button_data(83, "spring green"))
e83.place(x=1220, y=490)
e115 = tk1.Button(tk, text="Mc\n115", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                  command=lambda: display_button_data(115, "spring green"))
e115.place(x=1220, y=560)

# Group XVI
e8 = tk1.Button(tk, text="O\n8", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                command=lambda: display_button_data(8, "lemon chiffon"))
e8.place(x=1310, y=210)
e16 = tk1.Button(tk, text="S\n16", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                 command=lambda: display_button_data(16, "lemon chiffon"))
e16.place(x=1310, y=280)
e34 = tk1.Button(tk, text="Se\n34", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                 command=lambda: display_button_data(34, "lemon chiffon"))
e34.place(x=1310, y=350)
e52 = tk1.Button(tk, text="Te\n52", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(52, "medium spring green"))
e52.place(x=1310, y=420)
e84 = tk1.Button(tk, text="Po\n84", width=6, height=3, font=('Arial black', 10), relief="sunken",
                 bg="medium spring green",
                 command=lambda: display_button_data(84, "medium spring green"))
e84.place(x=1310, y=490)
e116 = tk1.Button(tk, text="Lv\n116", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="spring green",
                  command=lambda: display_button_data(116, "spring green"))
e116.place(x=1310, y=560)

# Group XVII
e9 = tk1.Button(tk, text="F\n9", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                command=lambda: display_button_data(9, "lemon chiffon"))
e9.place(x=1400, y=210)
e17 = tk1.Button(tk, text="Cl\n17", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="lemon chiffon",
                 command=lambda: display_button_data(17, "lemon chiffon"))
e17.place(x=1400, y=280)
e35 = tk1.Button(tk, text="Br\n35", width=6, height=3, font=('Arial black', 10), bg="lemon chiffon",
                 command=lambda: display_button_data(35, "lemon chiffon"))
e35.place(x=1400, y=350)
e53 = tk1.Button(tk, text="I\n53", width=6, height=3, font=('Arial black', 10), bg="lemon chiffon",
                 command=lambda: display_button_data(53, "lemon chiffon"))
e53.place(x=1400, y=420)
e85 = tk1.Button(tk, text="At\n85", width=6, height=3, font=('Arial black', 10), bg="lemon chiffon",
                 command=lambda: display_button_data(85, "lemon chiffon"))
e85.place(x=1400, y=490)
e117 = tk1.Button(tk, text="Ts\n117", width=6, height=3, font=('Arial black', 10), bg="lemon chiffon",
                  command=lambda: display_button_data(117, "lemon chiffon"))
e117.place(x=1400, y=560)

# Group XVIII
e2 = tk1.Button(tk, text="He\n2", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                command=lambda: display_button_data(2, "orange"))
e2.place(x=1490, y=140)
e10 = tk1.Button(tk, text="Ne\n10", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                 command=lambda: display_button_data(10, "orange"))
e10.place(x=1490, y=210)
e18 = tk1.Button(tk, text="Ar\n18", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                 command=lambda: display_button_data(18, "orange"))
e18.place(x=1490, y=280)
e36 = tk1.Button(tk, text="Kr\n36", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                 command=lambda: display_button_data(36, "orange"))
e36.place(x=1490, y=350)
e54 = tk1.Button(tk, text="Xe\n54", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                 command=lambda: display_button_data(54, "orange"))
e54.place(x=1490, y=420)
e86 = tk1.Button(tk, text="Rn\n86", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                 command=lambda: display_button_data(86, "orange"))
e86.place(x=1490, y=490)
e118 = tk1.Button(tk, text="Og\n118", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="orange",
                  command=lambda: display_button_data(118, "orange"))
e118.place(x=1490, y=560)

# Extra Elements I
e57 = tk1.Button(tk, text="La\n57", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(57, "Skyblue1"))
e57.place(x=230, y=710)
e58 = tk1.Button(tk, text="Ce\n58", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(58, "Skyblue1"))
e58.place(x=320, y=710)
e59 = tk1.Button(tk, text="Pr\n59", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(59, "Skyblue1"))
e59.place(x=410, y=710)
e60 = tk1.Button(tk, text="Nd\n60", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(60, "Skyblue1"))
e60.place(x=500, y=710)
e61 = tk1.Button(tk, text="Pm\n61", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(61, "Skyblue1"))
e61.place(x=590, y=710)
e62 = tk1.Button(tk, text="Sm\n62", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(62, "Skyblue1"))
e62.place(x=680, y=710)
e63 = tk1.Button(tk, text="Eu\n63", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(63, "Skyblue1"))
e63.place(x=770, y=710)
e64 = tk1.Button(tk, text="Gd\n64", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(64, "Skyblue1"))
e64.place(x=860, y=710)
e65 = tk1.Button(tk, text="Tb\n65", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(65, "Skyblue1"))
e65.place(x=950, y=710)
e66 = tk1.Button(tk, text="Dy\n66", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(66, "Skyblue1"))
e66.place(x=1040, y=710)
e67 = tk1.Button(tk, text="Ho\n67", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(67, "Skyblue1"))
e67.place(x=1130, y=710)
e68 = tk1.Button(tk, text="Er\n68", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(68, "Skyblue1"))
e68.place(x=1220, y=710)
e69 = tk1.Button(tk, text="Tm\n69", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(69, "Skyblue1"))
e69.place(x=1310, y=710)
e70 = tk1.Button(tk, text="Yb\n70", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="Skyblue1",
                 command=lambda: display_button_data(70, "Skyblue1"))
e70.place(x=1400, y=710)

# Extra Elements II
e89 = tk1.Button(tk, text="Ac\n89", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(89, "aquamarine"))
e89.place(x=230, y=780)
e90 = tk1.Button(tk, text="Th\n90", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(90, "aquamarine"))
e90.place(x=320, y=780)
e91 = tk1.Button(tk, text="Pa\n91", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(91, "aquamarine"))
e91.place(x=410, y=780)
e92 = tk1.Button(tk, text="U\n92", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(92, "aquamarine"))
e92.place(x=500, y=780)
e93 = tk1.Button(tk, text="Np\n93", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(93, "aquamarine"))
e93.place(x=590, y=780)
e94 = tk1.Button(tk, text="Pu\n94", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(94, "aquamarine"))
e94.place(x=680, y=780)
e95 = tk1.Button(tk, text="Am\n95", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(95, "aquamarine"))
e95.place(x=770, y=780)
e96 = tk1.Button(tk, text="Cm\n96", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(96, "aquamarine"))
e96.place(x=860, y=780)
e97 = tk1.Button(tk, text="Bk\n97", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(97, "aquamarine"))
e97.place(x=950, y=780)
e98 = tk1.Button(tk, text="Cf\n98", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(98, "aquamarine"))
e98.place(x=1040, y=780)
e99 = tk1.Button(tk, text="Es\n99", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                 command=lambda: display_button_data(99, "aquamarine"))
e99.place(x=1130, y=780)
e100 = tk1.Button(tk, text="Fm\n100", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                  command=lambda: display_button_data(100, "aquamarine"))
e100.place(x=1220, y=780)
e101 = tk1.Button(tk, text="Md\n101", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                  command=lambda: display_button_data(101, "aquamarine"))
e101.place(x=1310, y=780)
e102 = tk1.Button(tk, text="No\n102", width=6, height=3, font=('Arial black', 10), relief="sunken", bg="aquamarine",
                  command=lambda: display_button_data(102, "aquamarine"))
e102.place(x=1400, y=780)

tk.mainloop()
