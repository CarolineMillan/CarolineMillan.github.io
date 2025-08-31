---
layout: default
title: Home
---

# Welcome to {{ site.title }}

<div class="projects-gallery">
  {% for project in site.data.projects %}
    <div class="project-card">
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>{{ project.description }}</p>
    </div>
  {% endfor %}
</div>