const elements = document.querySelectorAll(
  ".x-el.c1-1.c1-2.c1-2k.c1-2l.c1-6u.c1-2z.c1-30.c1-6v.c1-6w.c1-6x.c1-6y.c1-6z.c1-70.c1-71.c1-72.c1-73.c1-74.c1-75.c1-76.c1-77.c1-78.c1-79.c1-7a.c1-7b.c1-7c.c1-7d.c1-7e.c1-7f.c1-7g.c1-7h.c1-7i.c1-7j.c1-7k.c1-7l.c1-7m.c1-s.c1-b.c1-7o.c1-c.c1-3t.c1-d.c1-7r.c1-e.c1-h.c1-i.x-rt"
);

const wineSection = elements[elements.length - 1];

console.log(wineSection);

wineSection.childNodes.forEach((node) => {
  console.log(node.innerText);
});
