'use strict';
/* Mecanismo Barabási-Albert puro, sem DOM. Mesma matemática da referência
   anexa_o_preferencial.html: roleta proporcional ao grau, raio agressivo
   com teto e escala de cor Turbo com domínio estendido. */
(function (host) {
  function mulberry32(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function pickTargets(rand, degrees, m) {
    var total = 0, i;
    for (i = 0; i < degrees.length; i++) { total += degrees[i]; }
    var targets = [], guard = 0;
    while (targets.length < m && targets.length < degrees.length && guard < 500) {
      guard++;
      var r = rand() * total, sum = 0, chosen = 0;
      for (i = 0; i < degrees.length; i++) {
        sum += degrees[i];
        if (r <= sum) { chosen = i; break; }
      }
      if (targets.indexOf(chosen) < 0) { targets.push(chosen); }
    }
    return targets;
  }
  function radius(degree) {
    return Math.min(120, 3 + Math.pow(degree, 1.15) * 0.6);
  }
  function colorFor(scale, degree) {
    var c = degree > 50 ? 50 : (degree < 1 ? 1 : degree);
    var t = 0.12 + 0.83 * ((c - 1) / 49);
    return scale(t);
  }
  function histogram(degrees) {
    var counts = {}, i, maxK = 1;
    for (i = 0; i < degrees.length; i++) {
      var d = degrees[i];
      if (d > 0) { counts[d] = (counts[d] || 0) + 1; if (d > maxK) { maxK = d; } }
    }
    var data = Object.keys(counts).map(function (key) { return { k: +key, freq: counts[key] }; });
    data.sort(function (a, b) { return a.k - b.k; });
    var maxFreq = 1, j;
    for (j = 0; j < data.length; j++) { if (data[j].freq > maxFreq) { maxFreq = data[j].freq; } }
    return { data: data, maxK: maxK, maxFreq: maxFreq };
  }
  host.BA = { mulberry32: mulberry32, pickTargets: pickTargets, radius: radius, colorFor: colorFor, histogram: histogram };
})(typeof window !== 'undefined' ? window : globalThis);
