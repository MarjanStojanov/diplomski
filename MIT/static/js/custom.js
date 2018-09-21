
function kontinenti()
{

  // funkcija za okretanje novcica
  //randomizuje sliku iz niza, postavlja je na novcic
  // i podesava odgovarajuci tekst
  var b=0
  niz=['static/imgs/coin/Evropa.jpg', 'static/imgs/coin/Azija.jpg', 'static/imgs/coin/J.Amerika.jpg' ,'static/imgs/coin/S.Amerika.jpg' ,'static/imgs/coin/Australija.jpg' ,'static/imgs/coin/Afrika.jpg']

  var card = document.getElementById('test')
  card.addEventListener( 'click', function()
   {
      card.classList.toggle('flpd')
    	b=Math.floor(Math.random() * 6)
    	setTimeout(function()
      {
    		document.getElementById('back').style.backgroundImage="url("+ niz[b] +")"
        document.getElementById('back').innerHTML=niz[b].split('coin/')[1].split('.jpg')[0]
    		document.getElementById('front').style.backgroundImage="url("+ niz[b] +")"
    		document.getElementById('front').innerHTML=niz[b].split('coin/')[1].split('.jpg')[0]

    	},300) //set timeout
  }); //event listener
}


function kontinent()
{
  //funkcija koja dohvata sve polaroide
  //i randomizuje njihovu lokaciju i ugao

    sto = document.getElementById("sto")

    polaroidi = document.getElementsByClassName("polaroid")

    for (i=0;i<polaroidi.length;i++)
    {

      top1 = '' + (Math.floor(Math.random() * 400 + 50)) + "px"
      left = '' + (Math.floor(Math.random() * 1400)) + "px"
      polaroidi[i].style.setProperty('left', left)
      polaroidi[i].style.setProperty('top', top1)
      polaroidi[i].style.setProperty('transform','rotate('+ Math.floor(Math.random() * 160 - 80)  +'deg)')
      polaroidi[i].style.setProperty('display','block')

    }
/*
  for (i=0;i<6;i++)
  {
      top1 = '' + (Math.floor(Math.random() * 400 + 50)) + "px"
      left = '' + (Math.floor(Math.random() * 1400)) + "px"
      div = document.createElement('div')
      div.setAttribute('class','polaroid')
      div.style.setProperty('left', left)
      div.style.setProperty('top', top1)
      div.style.setProperty('transform','rotate('+ Math.floor(Math.random() * 160 - 80)  +'deg)')

      img = document.createElement('img')
      img.setAttribute('class','slika_u_pol')
      img.src='../static/imgs/pozadina.jpg'
      div.append(img)

      h2 = document.createElement('h2')
      h2.innerHTML='BALI'
      div.append(h2)

      sto.append(div)
  }

*/
}


function drzava()
{


  destinacije = document.getElementsByClassName('glavni')
  levo = document.getElementsByClassName('levo')
  desno = document.getElementsByClassName('desno')
  destinacije[0].style.display='block'
  b = 0
  centar = document.getElementById('glavni')

    for(i=0;i<desno.length;i++)
    {
  alert(desno[i])
      desno[i].addEventListener('click',function()
      {
          centar.style.setProperty('opacity','0')

            destinacije[b].style.display='none'
            destinacije[b++].style.display='block'
          setTimeout(function()
          {
            centar.style.setProperty('opacity','1')
          },350)
      });

        levo[i].addEventListener('click',function()
        {
            centar.style.setProperty('opacity','0')

            destinacije[b].style.display='none'
            destinacije[b--].style.display='block'
            
            setTimeout(function()
            {
              centar.style.setProperty('opacity','1')
            },350)
        });
    }
  

    button = document.getElementById('klik')
    button.addEventListener('click', function(){ 

        btn = document.getElementById('saznaj')
        naslov = document.getElementById('naslov').innerHTML
        btn.href = '/destinacija/' + naslov.toLowerCase()

        btn.click()
    })




}




function otvori(a)
{
  //otvaranje zeljenog kontinenta na dvoklik
  //setovanje hrefa i aktiviranje click eventa na linku

  url = a.innerHTML.split('/coin/')[1].split('.jpg')[0]

  a.href = "/kontinent/" + url.toLowerCase().replace('.','') + "/drzave" //replace zbog s.amerika i j.amerika
  a.click()


}



function poseti(a)
{
  //otvaranje drzave po izboru
  dest = a.innerHTML.split('<h4>')[1].split('</h4>')[0]

  a.href = '/drzava/' + dest.toLowerCase().replace(' ','')
  a.click()
}


function destinacija(){
  cene = document.getElementsByClassName('cene')

  for (i=0;i<cene.length;i++)
    {
      cene[i].addEventListener('click', function(){
        if(this.innerHTML.includes('N/A'))
          return
              if (this.style.backgroundColor == 'yellow')
              {
                this.style.setProperty('background-color','transparent')
                this.style.setProperty('color','white')
              }
              else
              {
                this.style.setProperty('background-color','yellow')
                this.style.setProperty('color','black')
              }
        })
    }


  ter = document.getElementsByClassName('poldol')

  for (i=0;i<ter.length;i++)
    {
      ter[i].addEventListener('click', function()
      {
        if (this.style.backgroundColor == 'yellow')
        {
          this.style.setProperty('background-color','transparent')
          this.style.setProperty('color','white')
        }
        else
        {
          this.style.setProperty('background-color','yellow')
          this.style.setProperty('color','black')
        }
      })
    }
}


function pretraga(a)
{
  keyword = document.getElementById('searchbar')
  a.addEventListener('click',function(e){

  alert(keyword.value.toLowerCase())

 a.href = '/search/' + keyword.value.toLowerCase()
 a.click()
  })
}