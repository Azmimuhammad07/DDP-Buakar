from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'home.html')
def page2(request):
    return render(request, 'page2.html')
def about(request):
    return render(request, 'about.html')
def berita1(request):
    return render(request, 'berita/berita1.html')
def pagarlaut(request):
    return render(request, 'berita/pagarlaut.html')
def raffiahmad(request):
    return render(request, 'berita/raffiahmad.html')
def makansiang(request):
    return render(request, 'berita/makansiang.html')
def makansiang2(request):
    return render(request, 'berita/makansiang2.html')
def ppn(request):
    return render(request, 'berita/ppn.html')
def pagarlauttangerang(request):
    return render(request, 'berita/pagarlauttangerang.html')
def sayur(request):
    return render(request, 'berita/sayur.html')
def informatika(request):
    return render(request, 'berita/informatika.html')
def exchange_rate(request):
    return render(request, 'berita/exchange_rate.html')
def koinjagat(request):
    return render(request, 'berita/koinjagat.html')
def kalori(request):
    return render(request, 'kalori.html')
def otot(request):
    return render(request, 'otot.html')

def olahraga(request):
    return render(request, 'olahraga/olahraga.html')
def arsenal_krisis_stiker(request):
    return render(request, 'olahraga/arsenal_krisis_striker.html')
def prediksi_squad_timnas(request):
    return render(request, 'olahraga/prediksi_squad_timnas.html')
def maguire(request):
    return render(request, 'olahraga/maguire.html')
def pep_guardiola(request):
    return render(request, 'olahraga/pep_guardiola.html')
def nottingham(request):
    return render(request, 'olahraga/nottingham.html')
def bulutangkis(request):
    return render(request, 'olahraga/bulutangkis.html')




def exchange_rate(request):
    exchange_result = None

    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency_from = request.POST.get('currency_from')
        currency_to = request.POST.get('currency_to')

        # Jika amount dan kurs sudah diinputkan
        if amount and currency_from and currency_to:
            try:
                amount = float(amount)
                
                # Kurs contoh (dapat disesuaikan dengan kurs aktual atau API)
                exchange_rates = {
                    'USD': {'IDR': 15000, 'EUR': 0.95},  # USD ke IDR dan EUR
                    'IDR': {'USD': 0.67, 'EUR': 0.63},  # IDR ke USD dan EUR
                    'EUR': {'USD': 1.05, 'IDR': 16000},  # EUR ke USD dan IDR
                }

                if currency_from in exchange_rates and currency_to in exchange_rates[currency_from]:
                    rate = exchange_rates[currency_from][currency_to]
                    converted_amount = amount * rate
                    exchange_result = {
                        'original': amount,
                        'currency_from': currency_from,
                        'currency_to': currency_to,
                        'converted_amount': converted_amount,
                        'rate': rate
                    }
                else:
                    exchange_result = 'Kurs tidak tersedia.'
            except ValueError:
                exchange_result = 'Input tidak valid.'
    
    return render(request, 'exchange_rate.html', {'exchange_result': exchange_result})
