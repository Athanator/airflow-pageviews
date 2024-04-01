<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://airflow.apache.org/">
    <img src="https://pbs.twimg.com/media/EFOe7T4X4AEfIyl.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">airflow-pageviews-postgres</h3>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Deployment</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<div align="left">
</div>
<!-- ABOUT THE PROJECT -->
## About The Project

The Wikimedia Foundation (the organization behind Wikipedia) provides all pageviews since 2015 in machine-readable format. The pageviews can be downloaded in gzip format and are aggregated per hour per page. Each hourly dump is approximately 50 MB in gzipped text files and is somewhere between 200 and 250 MB in size unzipped.

This project is intended to build an Airflow-Orchestrated pipeline to ingest data from "Wikimedia Foundation", get pageviews KPIs and upload them into Postgres Database. The schedule interval is potentially to be set each hour.

The pipeline consists of 5 Dags:
1. get_data: Perform a call into webpage source (Wikimedia) and download the corresponding .gz file. This file containes all the number of views for each company. For this project, we will be focusing on the following companies: Amazon, Apple, Facebook, Google and Microsoft
2. extract_gz: Extract the .gz file into the selected destination folder
3. fetch_pageviews: As from the 5 selected companies, we extract the number of views for each company
4. create_pet_table: Create the postgres database over which the data will be inserted
5. Insert the data into the database


![image](https://github.com/Athanator/airflow-pageviews/assets/93158972/4156f23c-efc8-4104-9f3f-f2bb9bbd33c7)

![image](https://github.com/Athanator/airflow-pageviews/assets/93158972/627dcb3d-e8b2-4e58-9959-c6fb0b9e805d)

<div align="center">
    <a href="https://github.com/Athanator/airflow-pageview">
    <img src="https://github.com/Athanator/airflow-pageviews/assets/93158972/081b39c4-4036-4877-af9b-34d4d10b3c66" alt="Logo" >
  </a>

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>                                                                 


### Built With
<div align="left">


<ul>
    <li><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Logo" ></li>
    <li><img src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white" alt="Logo" ></li>
    <li><img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white" alt="Logo" ></li>
    <li><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Logo" ></li>
</ul>

</div>

!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to reproduce the Project

### Prerequisites

Install latest version of Dockerhub (https://docs.docker.com/desktop/install/)

### Deployment

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Open Docker Hub.
2. Clone the repo
   ```sh
   git clone https://github.com/Athanator/airflow-pageviews.git
   ```
3. Deploy containers
   ```sh
   docker compose up -d --build
   ```
4. In the Docker container (airflow-webserver-1), go to UI (port 8080:8080) and type "airflow" as login and password

5. Click on tab "Admin/Connections" and add the following connection. This is where the resulting data will be stored

![image](https://github.com/Athanator/airflow-pageviews/assets/93158972/25a78fa9-7540-400a-b0be-af783ea8c21d)

6. In the "DAGs" section, search for DAG "chapter4_stocksense_bashoperator" and execute it

![image](https://github.com/Athanator/airflow-pageviews/assets/93158972/709fbfda-a968-4c4c-a87c-11492d595f24)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/johan-steven-jaramillo-b6580a58
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
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
[Python-logo]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Postgres-logo]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
