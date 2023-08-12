function fetchareaData() {
    fetch('/area_data/')
    .then(response => response.json())
    .then(data => {
      renderBarChart(data);
    })
    .catch(error => {
      console.error('Error fetching top consignors data:', error);
    });
  }
  
  // Function to render the bar chart using ApexCharts
  function renderAreaChart(data) {
    const total_booking_monthwise = data.total_booking_sum_monthwise;
    const total_vehicle_freight_monthwise = data.total_vehicle_freight_sum_monthwise;
    const months = Object.keys(total_booking_monthwise).sort();
  
    var areaChartOptions = {
      series: [
        {
          name: 'Total Booking',
          data: months.map((month) => total_booking_monthwise[month]),
        },
        {
          name: 'Total Vehicle Freight',
          data: months.map((month) => total_vehicle_freight_monthwise[month]),
        },
      ],
      chart: {
        height: 350,
        type: 'area',
        toolbar: {
          show: false,
        },
      },
      colors: ["#4f35a1", "#246dec"],
      dataLabels: {
        enabled: false,
      },
      stroke: {
        curve: 'smooth'
      },
      labels: months.map((month) => getMonthName(month)), // Assuming you have a function getMonthName to get the month names.
      markers: {
        size: 0
      },
      yaxis: [
        {
          title: {
            text: 'Total Booking',
          },
        },
        {
          opposite: true,
          title: {
            text: 'Total Vehicle Freight',
          },
        },
      ],
      tooltip: {
        shared: true,
        intersect: false,
      }
    };
  
    var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
    areaChart.render();
  }
  
  // Function to get month names based on the month number (1 to 12)
  function getMonthName(monthNumber) {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return months[monthNumber - 1];
  }