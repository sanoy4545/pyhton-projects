import pikepdf

old_file=pikepdf.Pdf.open("receipt (Generated on 13_02_2024 10_40 PM).pdf")

n=pikepdf.Permissions(extract=False)

old_file.save("new.pdf",encryption= pikepdf.Encryption(user="1234",owner="abc",allow=n))
