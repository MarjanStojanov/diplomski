
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
  var destinacije = document.getElementsByClassName('glavni')
  var levo  = document.getElementsByClassName('levo')
  var desno = document.getElementsByClassName('desno')
  destinacije[0].style.display='block'
  var b = 0

    for(i=0;i<desno.length;i++)
    {
        desno[i].addEventListener('click',function()
        {
                  destinacije[b].style.opacity='0'
          if (b >= destinacije.length-1)
            b = destinacije.length-2
            destinacije[b].style.display='none'
            b++
            destinacije[b].style.display='block'
          setTimeout(function(){
            destinacije[b].style.opacity='1'
          },350)
})
        levo[i].addEventListener('click',function()
        {

          destinacije[b].style.opacity='0'
          if (b <= 0)
            b = 1
          destinacije[b].style.display='none'
          b--
          destinacije[b].style.display='block'

          setTimeout(function(){
            destinacije[b].style.opacity='1'
          },350)
        });
    }

        button = document.getElementsByClassName('klik')
        for (i=0;i<button.length;i++)
        {

              button[i].addEventListener('click', function(){

              btn = document.getElementsByClassName('saznaj')[i]
              naslov = document.getElementsByClassName('naslov')[i].innerHTML.replace(' ','')
              btn.href = '/destinacija/' + naslov.toLowerCase()

              btn[i].click()
          })
        }





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
              if (this.style.backgroundColor == '#ff5e13')
              {
                prevoz.replace(this.innerHTML,'')
                this.style.setProperty('background-color','transparent')
                this.style.setProperty('color','white')
              }
              else
              {
                prevoz += this.innerHTML
                this.style.setProperty('background-color','#ff5e13')
                this.style.setProperty('color','black')
              }
        })
    }

var prevoz = ''
var termin = ''

  ter = document.getElementsByClassName('poldol')

  for (i=0;i<ter.length;i++)
    {
      ter[i].addEventListener('click', function()
      {
        if (this.style.backgroundColor == '#ff5e13')
        {
          this.style.setProperty('background-color','transparent')
          this.style.setProperty('color','white')
        }
        else
        {
          for (i=0;i<ter.length;i++)
          {
            ter[i].style.setProperty('background-color','transparent')
            ter[i].style.setProperty('color','white')

          }
          termin = this.innerHTML
          this.style.setProperty('background-color','#ff5e13')
          this.style.setProperty('color','black')

        }
      })
    }
}


function pretraga(a)
{
  keyword = document.getElementById('searchbar')
  a.href = '/search/' + keyword.value.toLowerCase()
  a.click()
}




function token()
{

  $('#btnToken').click(function(){
    if (!(document.getElementById('email').value.includes('@')))
    {
      alert('email mora sadrzati @ i . posle @')
      return
    }
    $.post('/token',{ 'email': $('#email').val() }).done(function(data){

      $('#email').val(data.toString())
      $('#btnToken').attr('disabled', 'disabled')
      $('#btnToken').html('Maksimalno jedan token po email-u')
      $('#btnToken').css("background-color","red");
      $('h2').html('Token generisan!')
    })

  })
}







function kontakt_email(){
  $("#contact-form").on('submit', function(e) {
   e.preventDefault();


   $.ajax({
     type: 'POST',
     url: '/sendemail',
     contentType:'application/json',
     data: JSON.stringify({'name':$('#form_email').val(), 'subject':$('#form_need').val(),'surname':$('#form_lastname').val(),'email':$('#form_email').val(),'message':$('#form_message').val()}),
     success: function() {
       alert('ayy')
        $('.successmail').css('display','block')
     }
   });
 });

 $(".confirm").on('click',function(){
   $('.successmail').css('display','none')
 })
}
