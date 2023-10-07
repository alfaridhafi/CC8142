# # coding challange 8142

# # Muhammad Dhafi Alfaridzi
# # Odoo development class

# fungsi checkcats
def checkCats(CatsTuti,CatsNinig):
    return CatsTuti,CatsNinig

# data uji 1
print("data1")
print()
datatuti1 = [3,5,2,12,7]
datanining1 = [4,1,15,8,3]
data_tuti1,data_nining1 = checkCats(datatuti1,datanining1)

# 1. buat salinan dari array milik tuti, dan hapus usia kucing dari array yang disalin
dataCopy_tuti1 = data_tuti1.copy()
dataCopy_tuti1.remove(3)
dataCopy_tuti1.remove(12)
dataCopy_tuti1.remove(7)
# 2. array yang berisi data Tuti dan Data nining
data_gabungan1 = [dataCopy_tuti1,data_nining1]
# 3. tentukan itu kucing besar atau kucing kecil
numor = 1
for num in data_gabungan1:
    for number in num:
        if number > 3:
            print(f"kucing Nomor {numor} adalah Kucing Dewasa, dan berusia {number} tahun")
        else:
            print(f"kucing Nomor {numor} masih anak-anak")
        numor += 1

# data uji 2
print("-"*35)
print("data2")
print()
datatuti2 = [9,16,6,8,3]
datanining2 = [10,5,6,1,4]
data_tuti2,data_nining2 = checkCats(datatuti2,datanining2)
# 1. buat salinan dari array milik tuti, dan hapus usia kucing dari array yang disalin
dataCopy_tuti2 = data_tuti2.copy()
dataCopy_tuti2.remove(9)
dataCopy_tuti2.remove(8)
dataCopy_tuti2.remove(3)
# 2. array yang berisi data Tuti dan Data nining
data_gabungan2 = [dataCopy_tuti2,data_nining2]
# 3. tentukan itu kucing besar atau kucing kecil
numor2 = 1
for num in data_gabungan2:
    for number in num:
        if number > 3:
            print(f"kucing Nomor {numor2} adalah Kucing Dewasa, dan berusia {number} tahun")
        else:
            print(f"kucing Nomor {numor2} masih anak-anak")
        numor2 += 1
