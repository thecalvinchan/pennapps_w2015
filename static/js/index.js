var width = 960,
    height = 500;

var force = d3.layout.force()
    .size([width, height])
    .charge(-400)
    .linkDistance(60)
    .on("tick", tick);

var svg = d3.select(".wrapper").append("svg")
    .attr("width", width)
    .attr("height", height);

var link = svg.selectAll(".link"),
    node = svg.selectAll(".node");

var nodearray = [];
var linkarray = [];

d3.json("graph.json", function(error, graph) {
  nodearray = graph.nodes;
  linkarray = graph.links;
  force
      .nodes(nodearray)
      .links(linkarray)
      .start();

  link = link.data(force.links());

  link.enter().append("line")
      .attr("class", "link");

  
  node = node.data(force.nodes());
  node.enter().append("circle")
      .attr("class", "node")
      .attr("r", 12)
      .on("dblclick", dblclick);

    
});

function tick() {
  link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  node.attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
}

function dblclick(d) {
  console.log(d);
  var tempNode = {"x": 600, "y": 130}
  var newNodeArray = [tempNode];
  var newLinkArray = [{"source": d.index, "target": nodearray.length}];
  nodearray = nodearray.concat(newNodeArray);
  linkarray = linkarray.concat(newLinkArray);

  force
    .nodes(nodearray)
    .links(linkarray)
    .start();

  link = svg.selectAll(".link");
      node = svg.selectAll(".node");

  link = link.data(force.links());
  link.enter().append("line")
      .attr("class", "link");

  node = node.data(force.nodes());
  node.enter().append("circle").attr("class", "node")
      .attr("r", 12)
      .on("dblclick", dblclick);

  
  console.log(nodearray);
  console.log(linkarray);
}
