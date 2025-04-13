n = int(input("Siyahıdakı ədədlərin sayını daxil et: "))
B = [random.randint(5, 54) for _ in range(n)]
print("Yaradılmış siyahı:", B)
bolunenler = [x for x in B if x % 5 == 0]

if bolunenler:
    ededi_orta = sum(bolunenler) / len(bolunenler)
    print("5-ə tam bölünən ədədlərin ədədi ortası:", ededi_orta)
else:
    print("Siyahıda 5-ə tam bölünən ədəd yoxdur.")
