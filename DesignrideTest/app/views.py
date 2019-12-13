from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from app.models import Products


def UserDetail(request):
    try:
        ProName = request.POST.get("name")
        des = request.POST.get("des")
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(img.name,img)
            Products(ProductName=ProName, Description=des).save()
            res = Products.objects.all()
            return render(request, "index.html", {"data": res})
        except :
            return render(request,"user.html")

    except ValueError:
        return render(request, "user.html")


