---
title: Resources
permalink: /resources.html
---
<style>@import url("styles.css");</style>

<nav class="site-nav">
  <a class="brand" href="index.html">Hogenesch Lab</a>
  <a href="research.html">Research</a>
  <a href="people.html">People</a>
  <a href="publications.html">Publications</a>
  <a class="active" href="resources.html">Resources</a>
  <a href="join.html">Join</a>
</nav>

<header class="page-header">
  <p class="eyebrow">Resources</p>
  <h1>Tools, databases, and analysis frameworks</h1>
  <p class="lede">
    The lab's most durable field contributions are the methods and datasets other groups
    can use directly. This page keeps the list compact and focused.
  </p>
</header>

<div class="resource-grid">
  <div class="resource-card">
    <h2>JTK_CYCLE</h2>
    <p>A widely used nonparametric method for detecting rhythmic signals in genome-scale time-series data.</p>
    <p><a href="https://pubmed.ncbi.nlm.nih.gov/20876817/">Publication</a></p>
  </div>
  <div class="resource-card">
    <h2>MetaCycle</h2>
    <p>An integrated R package that combines ARSER, JTK_CYCLE, and Lomb-Scargle for periodicity analysis.</p>
    <p><a href="https://pubmed.ncbi.nlm.nih.gov/27378304/">Publication</a> · <a href="https://github.com/gangwug/MetaCycle">GitHub</a></p>
  </div>
  <div class="resource-card">
    <h2>CYCLOPS</h2>
    <p>A machine-learning framework for reconstructing temporal order and circadian phase from unordered samples.</p>
    <p><a href="https://pubmed.ncbi.nlm.nih.gov/28439010/">Publication</a></p>
  </div>
  <div class="resource-card">
    <h2>CircaDB</h2>
    <p>A searchable database of mammalian circadian gene-expression profiles built for bench and computational users.</p>
    <p><a href="https://pubmed.ncbi.nlm.nih.gov/23180795/">Publication</a> · <a href="http://circadb.org">Site</a></p>
  </div>
  <div class="resource-card">
    <h2>Gene Atlas and Gene Wiki</h2>
    <p>Large-scale expression mapping and community annotation resources that broaden functional genomics utility.</p>
    <p><a href="https://pubmed.ncbi.nlm.nih.gov/15075390/">Gene Atlas</a> · <a href="https://pubmed.ncbi.nlm.nih.gov/19755503/">Gene Wiki</a></p>
  </div>
  <div class="resource-card">
    <h2>SkinPhaser and Oslops</h2>
    <p>Skin-phase biomarker validation and population-ordering workflows that support human circadian medicine studies.</p>
    <p><a href="https://github.com/gangwug/SkinPhaser">SkinPhaser</a> · <a href="https://github.com/gangwug/Oslops">Oslops</a></p>
  </div>
</div>

## Notes on Use

- Use JTK_CYCLE or MetaCycle for rhythmicity detection in structured time-series experiments.
- Use CYCLOPS and related ordering workflows when sample time is missing or incomplete.
- Use CircaDB and atlas papers to identify tissue-specific rhythmic transcripts and phases.
- Use skin-based biomarker resources when the goal is translational phase estimation in humans.

<footer class="page-footer">
  <p>These resources are complemented by the reading list on <a href="publications.html">Selected Publications</a>.</p>
</footer>
