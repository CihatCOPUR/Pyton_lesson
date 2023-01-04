from django.shortcuts import render


kategori_liste= [
    'macera', 'romantik', ' dram' , 'horror'
]

film_liste= [
    {
        'film_adi':'film 1',
        'aciklama':'film 1 aciklama',
        'resim'  : "https://picsum.photos/id/684/600/400"
        },
          {
        'film_adi':'film 2',
        'aciklama':'film 2 aciklama',
        'resim'  : "https://picsum.photos/id/684/600/400"
        },
          {
        'film_adi':'film 3',
        'aciklama':'film 3 aciklama',
        'resim'  : "https://picsum.photos/id/684/600/400"
        }
]


# Create your views here.
def home(request):
    data= {
        'kategoriler' : kategori_liste ,
        'filmler ' : film_liste
    }
    return render(request , 'index.html', data)


def movies(request):
    data= {
        'filmler ' : film_liste }
    return render(request , 'movies.html' , data)