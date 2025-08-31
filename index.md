---
layout: default
title: Home
---

# Caroline Millan

Maths graduate turned software engineer.

Email: carolinemillan5678@gmail.com  
[GitHub](https://github.com/CarolineMillan)  
[LinkedIn](https://www.linkedin.com/in/caroline-millan/)

Here are a selection of projects, for all of them see [Projects](/projects).
<div class="projects-gallery">
  {% for project in site.data.projects %}
    <div class="project-card">
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>{{ project.description }}</p>
    </div>
  {% endfor %}
</div>