// https://cookstavern.com/menu

const elements = document.querySelectorAll(
  ".x-el.c1-1.c1-2.c1-2k.c1-2l.c1-6u.c1-2z.c1-30.c1-6v.c1-6w.c1-6x.c1-6y.c1-6z.c1-70.c1-71.c1-72.c1-73.c1-74.c1-75.c1-76.c1-77.c1-78.c1-79.c1-7a.c1-7b.c1-7c.c1-7d.c1-7e.c1-7f.c1-7g.c1-7h.c1-7i.c1-7j.c1-7k.c1-7l.c1-7m.c1-s.c1-b.c1-7o.c1-c.c1-3t.c1-d.c1-7r.c1-e.c1-h.c1-i.x-rt"
);

// wine section is the last element
const wineSection = elements[elements.length - 1];
let result = [];

// console.log(wineSection.childNodes);  // debugging

// indexes
// 1-10 is whites
// 14-17 sparkling
// 21-32 reds

// whites
for (let i = 1; i < 11; i++) {
  const s = wineSection.childNodes[i].textContent;
  result.push(s);
}

// sparkling
for (let i = 14; i < 18; i++) {
  const s = wineSection.childNodes[i].textContent;
  result.push(s);
}

// reds
for (let i = 21; i < 33; i++) {
  const s = wineSection.childNodes[i].textContent;
  result.push(s);
}

// replace nbsp with whitespace, replace fancy single quote and single quote with century
let s = result
  .join("\n")
  .replace(/\u00A0/g, " ")
  .replace(/‘/g, "20")
  .replace(/'/g, "20")
  .replace(/\.\d+/g, ""); // drop the cents

console.log(s);

/* Results
Columbard, Two Birds One Stone, FR 2022      8/32
Pinot Grigio, Cantina Colli Euganei, IT, 2023      9/34
Chenin Blanc, Painted Wolf, South Africa 2022      10/38
Albarino, Slope Life, Royal Slope, WA 2023      11/42
Sauvignon Blanc, Sodo Cellars, HHH, WA 2022      12/46
Viognier Blend, Gard, Royal Slope, WA 2022      12/48
Chardonnay, Bin 5757 Bennet Valley, CA 2021      11/42
Chardonay, Gehricke, Russian River Valley, CA 2021      56
Orange Gold, Gerard Bertrand, FR 2021      49
Rose, Kind Stranger , Columbia Valley, WA 2023      11/44
Rose Proseco, Lovo, IT 2021      11/42
Proseco, Guinigi, IT N/V      12/46
Cremant de Bourgogne Brut, Patriarche, NV FR      49
Brut Grand Cordon, Mumms, NV, FR      65
Pinot Noir, Casas del Bosques, CH 2022      10/38
Pinot Noir, Bin 5757, Bennet Valley, CA, 2021      48
Temperanillo, Bodega mas Que Vios, SP 2022      10/38 
Rioja, Cortijo Estate, SP 2021      11/42
Red Blend, Oak Grove, CA 2022      9/34
Granacha, Handwork, SP 2021      10/40
GSM, Sodo Cellars, Columbia Valley, WA 2022      12/46
Merlot, Weather Station, Columbia, WA 2021      11/42
Cabernet, Slope Life, Royal Slope, WA 2020      10/40
Cabernet, Lydian, Columbia Valley, WA 2022      52
Cab Franc, No es Pituko, Chile 2022      11/42
Petite Sirah, Guenoc, CA 2017      9/36
*/
