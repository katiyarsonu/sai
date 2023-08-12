// bar_chart_script.js
var barChartOptions = {
    series: [{
      data:  [10, 8, 6, 4, 2]  // Placeholder for dynamic data
    }],
    chart: {
      type: 'bar',
      height: 350,
      toolbar: {
        show: false
      },
    },
    colors: [
      "#246dec",
      "#cc3c43",
      "#367952",
      "#f5b74f",
      "#4f35a1"
    ],
    plotOptions: {
      bar: {
        distributed: true,
        borderRadius: 4,
        horizontal: false,
        columnWidth: '40%',
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    xaxis: {
      categories: ["Laptop", "Phone", "Monitor", "Headphones", "Camera"],  // Placeholder for dynamic x-axis labels
    },
    yaxis: {
      title: {
        text: "Grand Total Booking"  // Update y-axis title
      }
    }
  };
  
  
  // Make an AJAX request to retrieve data and render the chart
  /*$.ajax({
    url: '/get_top_consignors/',  // Replace with your Django URL
    method: 'GET',
    success: function(response) {
      var topConsignors = response.topConsignors;
      var topBookingValues = response.topBookingValues;
  
      // Update the x-axis categories and series data
      barChartOptions.xaxis.categories = topConsignors;
      barChartOptions.series[0].data = topBookingValues;
  
      // Initialize and render the chart
      var chart = new ApexCharts(document.querySelector("#chart"), barChartOptions);
      chart.render();
    },
    error: function(error) {
      console.error("Error fetching data:", error);
    }
  }); */
  