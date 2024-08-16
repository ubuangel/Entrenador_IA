


<a name="readme-top"></a>




<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<a href="https://github.com/ubuangel/Entrenador_IA">
    <!--<img src="images/pistola.jpg" alt="Logo" width="80" height="80">-->
  </a>

<h3 align="center">Virtual Curl IA</h3>


  <p align="center">

   <br />
    <a href="https://github.com/ubuangel/Entrenador_IA"><strong>Explora los documentos »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ubuangel/Entrenador_IA">Ver Demo</a>
    ·
    <a href="https://github.com/ubuangel/Entrenador_IA/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/ubuangel/Entrenador_IA/issues">Request Feature</a>
    
  
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#Sobre-este-Proyecto">Sobre Este Proyecto</a>
      <ul>
        <li><a href="#construido--con">Construido Con</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalacion">Instalacion</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contribuciones</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#acknowledgments">Agradecimientos</a></li>
  </ol>
</details>





<!-- ABOUT THE PROJECT -->
## Sobre este Proyecto

Un proyecto de visión por computadora tiene como objetivo crear un entrenador virtual para el ejercicio biceps de brazo utilizando 33 puntos de referencia detectados mediante un modelo de estimación de postura de la parte superior del cuerpo para contar los curl durante el ejercicio, detectar la mano que trabaja actualmente, detectar la posición incorrecta del codo , detectar la postura del cuerpo durante el ejercicio y realizar una rutina  sencilla para realizar el ejercicio completo


### Si se detecta una posición incorrecta del codo:-
   El entrenador de IA muestra un mensaje de advertencia
   El contador no aumenta

### Si el peso es pesado y el entrenador está en los primeros 6 curl:-
   El entrenador de IA sugiere un peso más ligero

### Si el peso es pesado y el entrenador está en los últimos 4 curl:-
   El entrenador de IA da un mensaje de apoyo

Sólo funciona cuando la mano detectada es la misma que la mano deseada

El entrenador de IA se puede utilizar como asistente de entrenamiento en salas de gimnasio o como alternativa para hacer ejercicio adecuado en casa.ga

![Descripción de la imagen Markdown](/images/traking.png)






<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



### Construido  Con

 
   * mediapipe
   * opencv
   * numpy
   * time 
   * playsound 
   * SO  GNU/Linux Debian 12 
<!--* [![Unity]][Unity-url]-->
<!--* [![Bootstrap][Bootstrap.com]][Bootstrap-url]-->


<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


Para poner en funcionamiento una copia local, siga estos sencillos pasos de ejemplo.




### Prerequisitos



* Conda




### Instalacion





1. Clona el repositorio
   ```sh
   git clone https://github.com/ubuangel/Entrenador_IA.git
   ```

2. En el directorio Raiz

```sh
  sudo apt-get update && sudo apt-get upgrade
  conda activate mientorno
  python TrainerLoop.py
  
  ```

<!--![imagen1][imagen1]-->

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



<!-- USAGE EXAMPLES -->

## Uso

Después de la instalación, se importa al proyecto :

![Descripción de la imagen Markdown](/images/ini.png)

![Descripción de la imagen Markdown](/images/entre.png)



<!-- ![Descripción de la imagen Markdown](/images/consola.png)-->


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [X] Spanish

Consulte los [problemas abiertos](https://github.com/ubuangel/Entrenador_IA/issues) para obtener una lista completa de las funciones,caracteristicas propuestas (y problemas conocidos).

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Las contribuciones son las que hacen de la comunidad de código abierto un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será **muy apreciada**.

Si tiene alguna sugerencia que pueda mejorar esto, bifurque el repositorio y cree una solicitud de extracción Pull Request. También puedes simplemente abrir un problema con la etiqueta "mejora "(enhancement).
¡No olvides darle una estrella al proyecto! ¡Gracias de nuevo!

1. Forkea
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>






<!-- CONTACT -->
## Contacto

Angel Bejar - abebe202023@gmail.com

Link del Proyecto: [https://github.com/ubuangel/Entrenador_IA](https://github.com/ubuangel/Entrenador_IA)

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



<!-- ACKNOWLEDGMENTS 
## Acknowledgments

Credito a

* [Youtube](https://www.youtube.com/watch?v=KTPh5Cryl24)


<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>  -->
 


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ubuangel/Entrenador_IA.svg?style=for-the-badge
[contributors-url]: https://github.com/ubuangel/Entrenador_IA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ubuangel/Entrenador_IA.svg?style=for-the-badge
[forks-url]: https://github.com/ubuangel/Entrenador_IA/network/members
[stars-shield]: https://img.shields.io/github/stars/ubuangel/Entrenador_IA.svg?style=for-the-badge
[stars-url]: https://github.com/ubuangel/Entrenador_IA/stargazers
[issues-shield]: https://img.shields.io/github/issues/ubuangel/Entrenador_IA.svg?style=for-the-badge
[issues-url]: https://github.com/ubuangel/Entrenador_IA/issues
[license-shield]: https://img.shields.io/github/license/ubuangel/Entrenador_IA.svg?style=for-the-badge
[license-url]: https://github.com/ubuangel/Entrenador_IA/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/angel-andres-bejar-merma-5baaba281
[product-screenshot]: images/resultado1.png
[Unity]: https://img.shields.io/badge/UNITY

<!--[imagen1]: images/pantallaso.png-->
[Unity-url]: https://unity.com/es
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
