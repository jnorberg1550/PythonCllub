% extends 'base.html' %}
{% block content %}
<h2>Products</h2>
<table class="table">
  <tr>
      <th>Meeting Title</th>
      <th>Meeting Location</th>
  </tr
  {% for p in meetingtype_list %}
    <tr>
      <td><a href="{% url 'meetingtupes' id=p.id %}">{{ p.meetingtitle }}</a></td>
     <td> {{p.meetinglocation }}</td>
    </tr>
    {% endfor %}

</table>
{% endblock %}
<ul class="nav navbar-nav">
    <li><a href="{% url 'types' %}">Meeting Titles</a></li>
    <li><a href="{% url 'location' %}">Location</a></li>
               
 </ul>
