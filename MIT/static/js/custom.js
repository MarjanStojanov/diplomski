
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
  b = 0
  temp_niz = ['t1','t2','t3','t4']
  centar = document.getElementById('glavni')
  desno  = document.getElementById('desno')
  levo   = document.getElementById('levo')
  naslov = document.getElementById('naslov')
  tekst  = document.getElementById('tekst')
//TODO: XMLhttpRequest get all images on page onload and put them in array

  desno.addEventListener('click',function()
  {
      centar.style.setProperty('opacity','0')
      naslov.innerHTML=temp_niz[b++]
      tekst.innerHTML = Math.random()
      setTimeout(function()
      {
        centar.style.setProperty('opacity','1')
      },350)
  });

    levo.addEventListener('click',function()
    {
        centar.style.setProperty('opacity','0')
        naslov.innerHTML=temp_niz[b--]
        tekst.innerHTML = Math.random()
        setTimeout(function()
        {
          centar.style.setProperty('opacity','1')
        },350)
    });
}




function otvori(a)
{
  //otvaranje zeljenog kontinenta na dvoklik
  //setovanje hrefa i aktiviranje click eventa na linku

  url = a.innerHTML.split('/coin/')[1].split('.jpg')[0]

  a.href = "/kontinent/" + url.toLowerCase().replace('.','') + "/drzave" //zbog s.amerika i j.amerika
  a.click()


}
