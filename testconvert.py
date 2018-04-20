from PIL import Image

im = Image.open("/home/koblitzj/git_projects/mine/PDF-Tool/puppies/0 fHFNrpv.jpg")

im.save("./puppies/TESTOUT.pdf", "PDF", resolution=100.0)