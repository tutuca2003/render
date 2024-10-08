from django.shortcuts import render, redirect
from .models import Agente, Compensatorio, Vacaciones, Articulo
from django.db.models import Sum, Count, F, Case, When, Value, IntegerField, Subquery
import datetime

# Create your views here.
def home(request):
    listagentes = Agente.objects.all() 
    return render(request, "Abmagentes.html", {"agentes":listagentes})

def registrarAgente(request):
    legajo=request.POST['legajo']
    nombre=request.POST['nombre']
    agente = Agente.objects.create(legajo=legajo, nombre=nombre)
    return redirect('/')

def edicionAgente(request, legajo):
    agente = Agente.objects.get(legajo=legajo)
    return render(request,"edicionAgente.html",{"agente":agente})

def editarAgente(request):
    legajo=request.POST['legajo']
    nombre=request.POST['nombre']
    agente = Agente.objects.get(legajo=legajo)
    agente.legajo= legajo 
    agente.nombre= nombre
    agente.save()
    return redirect('/')


def eliminarAgente(request, legajo):
    agente = Agente.objects.get(legajo=legajo)
    agente.delete()
    return redirect('/')


def compensatorio(request, legajo):
    #listado = Compensatorio.objects.all() 
    listado = Compensatorio.objects.filter(legajo=legajo).order_by('diaCompensatorio')
    datosagente = Agente.objects.get(legajo=legajo)
    #print(datosagente.nombre)
    suma = 0
    resta = 0
    total = 0
    for c in listado:
        if c.motivo == 0:
            suma += c.horas
        else:
            resta += c.horas
    total = (suma - resta)
    return render(request, "compensatorios.html", {"listado":listado, "total":total, "datosagente":datosagente})


def vacaciones(request, legajo):
    listado = Vacaciones.objects.filter(legajo=legajo)
    datosagente = Agente.objects.get(legajo=legajo)
    suma, resta, total = 0,0,0
    for c in listado:
        if c.motivo == 0:
            suma += c.dias
        else:
            resta += c.dias
    total = (suma - resta)
    return render(request, "vacaciones.html", {"listado":listado, "total":total, "datosagente":datosagente})


def articulos(request, legajo):
    #listado = Compensatorio.objects.all() 
    listado = Articulo.objects.filter(legajo=legajo)
    datosagente = Agente.objects.get(legajo=legajo)
    suma = 0
    resta = 0
    total = 0
    for c in listado:
        print(c.cantidadDias, c.cantidadHoras, c.id, c.legajo, datosagente.legajo, legajo)
     #   if c.motivo == 0:
      #      suma += c.dias
       # else:
        #    resta += c.dias
    #total = (suma - resta)
    return render(request, "articulos.html", {"listado":listado, "total":total, "datosagente":datosagente})


def articulosPantalla(request, ide):
    listado = Articulo.objects.filter(id=ide)
    for c in listado:
        datosagente = Agente.objects.get(nombre=c.legajo)
        print(c.legajo, c.id)
        diaC=(format(c.diaCreacion.day))
        mesC=(format(c.diaCreacion.month))
        añoC=(format(c.diaCreacion.year))
        diaA=(format(c.diaArticulo.day))
        mesA=(format(c.diaArticulo.month))
        añoA=(format(c.diaArticulo.year))
        cd, chs, cod, cohs,art155hs,art155d,ped,pehs,cjd,cjhs,dsd,dshs="","","","","","","","","","","",""
        loa,lpm,lpmh, lpnh,le,lpf,gp,com,art155, = "","","","","","","","",""
    if c.permiso == 0 :
       com=c.com
       if c.cantidadDias is None:
            cd=""
            chs=c.cantidadHoras 
       else:    
            cd=c.cantidadDias
            chs=""
               
    elif c.permiso == 1 :
        com=c.com
        if c.cantidadDias is None:
            cod=""
            cohs=c.cantidadHoras 
        else:    
            cod=c.cantidadDias
            cohs=""
        
    elif c.permiso == 2 :
        art155=c.art155        
        if c.cantidadDias is None:
            art155d=""
            art155hs=c.cantidadHoras 
        else:    
            art155d=c.cantidadDias
            art155hs=""
        
    elif c.permiso == 3 :
        com=c.com
        if c.cantidadDias is None:
            ped=""
            pehs=c.cantidadHoras 
        else:    
            ped=c.cantidadDias
            pedhs=""
        
    elif c.permiso == 4 :
        if c.cantidadDias is None:
            cjd=""
            cjhs=c.cantidadHoras 
        else:    
            cjd=c.cantidadDias
            cjhs=""
    elif c.permiso == 5 :
        if c.cantidadDias is None:
            dsd=""
            dshs=c.cantidadHoras 
        else:    
            dsd=c.cantidadDias
            dshs=""
    elif c.permiso == 6 :
        loa=c.cantidadDias
    elif c.permiso == 7 :
        lpm=c.cantidadDias
    elif c.permiso == 8 :
        lpmh=c.cantidadDias
    elif c.permiso == 9 :
        lpnh=c.cantidadDias
    elif c.permiso == 10 :
        le=c.cantidadDias
    elif c.permiso == 11 :
        lpf=c.cantidadDias
        gp=c.parentesco

    return render(request, "articulosPantalla.html", {"datosagente":datosagente,"listado":listado, "diaC":diaC,
                                                      "mesC":mesC, "añoC":añoC, "diaA":diaA, "mesA":mesA,"añoA":añoA,
                                                      "cd":cd, "chs":chs, "cod":cod, "cohs":cohs, "art155d":art155d, "art155hs":art155hs,
                                                      "ped":ped, "pehs":pehs, "cjd":cjd,"cjhs":cjhs,"dsd":dsd,"dshs":dshs, "loa":loa,
                                                      "lpm":lpm, "lpmh":lpmh, "lpnh":lpnh, "le":le, "lpf":lpf,"gp":gp,"com":com, "art155":art155})    


def mecanica(request, area):
    #listsector = Sector.objects.all()
    #listagentes = Agente.objects.filter(area__lte=8).order_by('area')
    #print(listsector) 
    listagentes = Agente.objects.filter(area=area)
    return render(request, "mecanica.html", {"agentes":listagentes})

def obraCivil(request):
    #listsector = Sector.objects.all()
    listagentes = Agente.objects.filter(area=9)
    #print(listsector) 
    return render(request, "obraCivil.html", {"agentes":listagentes})

def electricidad(request):
    #listsector = Sector.objects.all()
    listagentes = Agente.objects.filter(area=10).order_by('legajo')
    #print(listsector) 
    return render(request, "electricidad.html", {"agentes":listagentes})    

def otrasPlantas(request):
    #listsector = Sector.objects.all()
    listagentes = Agente.objects.filter(area=12).order_by('legajo')
    #print(listsector) 
    return render(request, "otrasPlantas.html", {"agentes":listagentes})       


def compensatorioTotal(request):
    
    listado = (Compensatorio.objects.select_related('legajo')
              .values('legajo', 'legajo__nombre')
              .annotate(
                  total_horas=Sum(
                      Case(
                          When(motivo=0, then='horas'),
                          default=-F('horas'),
                          output_field=IntegerField()
                      )
                  )
              )
              .order_by('legajo'))
    
    return render(request, "compensatoriosTotal.html", {"listado":listado})


def articuloTotal(request):
    fecha_busqueda = datetime.date(2024, 6, 30)
    listado = (Articulo.objects.select_related('legajo')
              .values('legajo', 'legajo__nombre','diaArticulo')
              .filter(diaArticulo__gt = fecha_busqueda, permiso=3)
              .order_by('-diaArticulo'))
    print(listado)

    return render(request, "articulosTotal.html", {"listado":listado})

def articuloNitro(request):
    
    listado = (Articulo.objects.select_related('legajo')
              .values('legajo', 'legajo__nombre','nitro')
              .filter(permiso=3, nitro__range=(2,12))
              .order_by('legajo__nombre', 'nitro'))
    #print(listado)
    dic={}
    lista=[]
    s=0
    for n in listado:
        if s==0:
            legajo= n['legajo']
            s=1
        if legajo == n['legajo']:
           lista.append( n['nitro'])
           dic[n['legajo__nombre']]=lista
           #print(n['legajo__nombre'])
       
        else:
           lista=[]
           lista.append( n['nitro'])
           dic[n['legajo__nombre']]=lista
        legajo= n['legajo'] 
    
   # print(dic.get(n['legajo'])[0])

    meses = list(range(2, 13))
  
    return render(request, "articulosNitro.html", {"listado":listado, 'dic':dic, 'meses':meses})


def vacacioneTotal(request):
    
    listado = (Vacaciones.objects.select_related('legajo')
              .values('legajo', 'legajo__nombre')
              .annotate(
                  total_horas=Sum(
                      Case(
                          When(motivo=0, then='dias'),
                          default=-F('dias'),
                          output_field=IntegerField()
                      )
                  )
              )
              .order_by('legajo'))
    
    return render(request, "vacacionesTotal.html", {"listado":listado})
