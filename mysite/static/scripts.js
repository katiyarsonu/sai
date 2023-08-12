// SIDEBAR TOGGLE

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
  if(!sidebarOpen) {
    sidebar.classList.add("sidebar-responsive");
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if(sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}



// ---------- CHARTS ----------

// BAR CHART
/*var barChartOptions = {
  series: [{
    data: [10, 8, 6, 4, 2]
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
    categories: ["Laptop", "Phone", "Monitor", "Headphones", "Camera"],
  },
  yaxis: {
    title: {
      text: "Count"
    }
  }
};

var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
barChart.render();
*/
// This function sends an HTTP GET request to the server to fetch top consignor data.
function fetchTopConsignorsData() {
  fetch('get_top_consignors/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(response => response.json())
  .then(data => {
    renderBarChart(data.topConsignors, data.topBookingValues);
  })
  .catch(error => {
    console.error('Error fetching top consignors data:', error);
  });
}

// Function to render the bar chart using ApexCharts
function renderBarChart(topConsignors, topBookingValues) {
  var barChartOptions = {
    series: [{
      data: topBookingValues // Use the fetched booking values here
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
      categories: topConsignors, // Use the fetched consignor labels here
    },
    yaxis: {
      title: {
        text: "Total Business"
      }
    }
  };

  var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
  barChart.render();
}

// Fetch the top consignor data and render the bar chart on page load
document.addEventListener('DOMContentLoaded', fetchTopConsignorsData);



// AREA CHART
/*var areaChartOptions = {
  series: [{
    name: 'EXPENSE',
    data: [31, 40, 28, 51, 42, 109, 100]
  }, {
    name: 'INCOME',
    data: [11, 32, 45, 32, 34, 52, 41]
  }],
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
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
  markers: {
    size: 0
  },
  yaxis: [
    {
      title: {
        text: 'EXPENSE',
      },
    },
    {
      opposite: true,
      title: {
        text: 'INCOME',
      },
    },
  ],
  tooltip: {
    shared: true,
    intersect: false,
  }
};

var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
areaChart.render(); */