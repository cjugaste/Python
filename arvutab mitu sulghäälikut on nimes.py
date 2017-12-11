#Cassandra Jugaste 10IT
nimi = input("Sisestage oma nimi: ")
k_täht = nimi.count("k")
g_täht = nimi.count("g")
d_täht = nimi.count("d")
t_täht = nimi.count("t")
p_täht = nimi.count("p")
b_täht = nimi.count("b")
K_täht = nimi.count("K")
G_täht = nimi.count("G")
D_täht = nimi.count("D")
P_täht = nimi.count("P")
B_täht = nimi.count("B")
T_täht = nimi.count("T")
sulghäälikud = k_täht + g_täht + d_täht + t_täht + p_täht + b_täht + K_täht + G_täht + D_täht + P_täht + B_täht + T_täht

print("Teie nimes olevate sulghäälikute arv on " + str(sulghäälikud) + ".")