const fs = require("fs");

// menu endpoint: http://bw-winelist-website-prod.s3-website-us-west-2.amazonaws.com/88e2ea0c-8997-4294-a420-bbe671780f25-prod/menu-88e2ea0c-8997-4294-a420-bbe671780f25.json?nocache=1730666419781

// carefull hitting this, prefer reading the info in from jeanty.json
async function getMenu() {
  const endpoint =
    "http://bw-winelist-website-prod.s3-website-us-west-2.amazonaws.com/88e2ea0c-8997-4294-a420-bbe671780f25-prod/menu-88e2ea0c-8997-4294-a420-bbe671780f25.json?nocache=1730666419781";

  const res = await fetch(endpoint);
  const data = await res.json();
  return data;
}

function saveFile(text, path) {
  fs.writeFile(path, text, (err) => {
    if (err) {
      console.error(err);
    } else {
      // file written successfully
    }
  });
}

async function generateTextFile(menu) {
  let s = [];

  menu
    .filter((item) => item.header1 == "Full Bottles")
    .map((item) => {
      // not using all this info atm but its here just in case
      const varietal = item.header2.trim();
      const name = item.name.trim();
      const vintage = item.vintage.trim();
      const price = item.price;

      s.push(`${name}  ${vintage}   $${price}`);
    });

  saveFile(s.join("\n"), "./Jeanty.txt");
}

async function main() {
  const menu = await getMenu();
  generateTextFile(menu);
}

main();
