<script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);
      function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country',   'Latitude'],
          ['Algeria', Math.floor((Math.random() * 10) + 1)], ['Angola', Math.floor((Math.random() * 10) + 1)], ['Benin', Math.floor((Math.random() * 10) + 1)], ['Botswana', Math.floor((Math.random() * 10) + 1)],
          ['Burkina Faso', Math.floor((Math.random() * 10) + 1)], ['Burundi', Math.floor((Math.random() * 10) + 1)], ['Cameroon', Math.floor((Math.random() * 10) + 1)],
          ['Canary Islands', Math.floor((Math.random() * 10) + 1)], ['Cape Verde', 15],
          ['Central African Republic', 4], ['Ceuta', Math.floor((Math.random() * 10) + 1)], ['Chad', 12],
          ['Comoros', Math.floor((Math.random() * 10) + 1)], ['Cote d\'Ivoire', 6],
          ['Democratic Republic of the Congo', Math.floor((Math.random() * 10) + 1)], ['Djibouti', 12],
          ['Egypt', Math.floor((Math.random() * 10) + 1)], ['Equatorial Guinea', 3], ['Eritrea', Math.floor((Math.random() * 10) + 1)],
          ['Ethiopia', 9], ['Gabon', 0], ['Gambia', 13], ['Ghana', 5],
          ['Guinea', 10], ['Guinea-Bissau', 12], ['Kenya', -1],
          ['Lesotho', Math.floor((Math.random() * 10) + 1)], ['Liberia', 6], ['Libya', 12], ['Madagascar', null],
          ['Madeira', 3], ['Malawi', Math.floor((Math.random() * 10) + 1)], ['Mali', 12], ['Mauritania', 18],
          ['Mauritius', -20], ['Mayotte', Math.floor((Math.random() * 10) + 1)], ['Melilla', Math.floor((Math.random() * 10) + 1)],
          ['Morocco', Math.floor((Math.random() * 10) + 1)], ['Mozambique', Math.floor((Math.random() * 10) + 1)], ['Namibia', -2],
          ['Niger', 14], ['Nigeria', 8], ['Republic of the Congo', -1],
          ['Réunion', -1], ['Rwanda', -2], ['Saint Helena', -16],
          ['São Tomé and Principe', 0], ['Senegal', 15],
          ['Seychelles', -5], ['Sierra Leone', 8], ['Somalia', 2],
          ['Sudan', 15], ['South Africa', Math.floor((Math.random() * 10) + 1)], ['South Sudan', 5],
          ['Swaziland', Math.floor((Math.random() * 10) + 1)], ['Tanzania', -6], ['Togo', 6], ['Tunisia', 6],
          ['Uganda', 1], ['Western Sahara', Math.floor((Math.random() * 10) + 1)], ['Zambia', Math.floor((Math.random() * 10) + 1)],
          ['Zimbabwe', Math.floor((Math.random() * 10) + 1)], ['United States', 4], ['China', Math.floor((Math.random() * 10) + 1)], ['Russia', Math.floor((Math.random() * 10) + 1)], ['Brazil', Math.floor((Math.random() * 10) + 1)], ['Chile', 12], ['New Zealand', Math.floor((Math.random() * 10) + 1)], ['Philippines', -3], ['Greenland', Math.floor((Math.random() * 10) + 1)]
        ]);


        var options = {
          colorAxis: {colors: ['#E3B505', '#95190c', '#610345', '#107e7d', '#044B7F', '#c4504a', '#af97de']},
          backgroundColor: '#81d4fa',
          defaultColor: '#f5f1df',
          legend: 'none',
        };

        var chart = new google.visualization.GeoChart(document.getElementById('geochart-colors'));
        chart.draw(data, options);
      };
    </script>

     <div id="geochart-colors" style=center></div>