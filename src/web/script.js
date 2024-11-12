// Load and render the plot
fetch("../../data/embeddings.json")
  .then(response => response.json())
  .then(data => {
    // Extract filenames and embeddings
    const filenames = Object.keys(data);
    const embeddings = Object.values(data);

    if (embeddings.length < 2) {
      document.getElementById("plot").innerHTML = "Not enough data to plot.";
      return;
    }

    // Extract and organize 2D coordinates from embeddings (x, y)
    const x_coords = embeddings.map(e => e[0]);
    const y_coords = embeddings.map(e => e[1]);

    // Define trace for Plotly scatter plot
    const trace = {
      x: x_coords,
      y: y_coords,
      mode: "markers+text",
      type: "scatter",
      text: filenames.map(name => name.split('.')[0]), // Display filename labels
      textposition: "top center",
      marker: { size: 8, color: 'blue' }
    };

    const layout = {
      title: "2D Embedding Visualization",
      xaxis: { title: "Dimension 1" },
      yaxis: { title: "Dimension 2" },
      showlegend: false
    };

    // Render the plot
    Plotly.newPlot("plot", [trace], layout);
  })
  .catch(error => {
    console.error("Error loading the embeddings data:", error);
  });
