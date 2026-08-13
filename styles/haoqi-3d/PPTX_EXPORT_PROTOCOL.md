# Haoqi 3D → Editable PPTX Export Protocol

Use this contract when creating or extending a Haoqi 3D deck. It removes assumptions about slide count and Three.js object names.

## Runtime contract

Expose `window.__PPTX_EXPORT__` from the deck:

```js
window.__PPTX_EXPORT__ = {
  version: 1,
  pageCount: () => PAGES.length,
  objectsForPage: pageIndex => ['hero-logo', 'product-model'],
  apply: pageIndex => { /* isolate background or selected object */ }
};
```

The bundled `demo.html` already implements this contract and provides:

```js
registerPptx3D(object3D, 'stable-id', { pages: [0, 2, 5] });
```

- Pass any `THREE.Object3D`: mesh, group, imported GLTF scene, text, particles, or a custom procedural model.
- Use a unique stable ID.
- Pass zero-based `pages` when the object only belongs to selected slides.
- Omit `pages` when it belongs to every slide.
- Register every 3D object that should remain independently movable in PowerPoint.
- Leave lighting, environment, floor, shadows, and non-editable scenery unregistered; they stay in the background layer.

Example:

```js
const product = new THREE.Group();
product.add(bodyMesh, logoMesh, detailMesh);
scene.add(product);
registerPptx3D(product, 'hero-product', { pages: [0, 4] });

const chart = scene.add(new THREE.Mesh(chartGeo, chartMat));
registerPptx3D(chart, '3d-chart', { pages: [6] });
```

A registered `Group` exports as one transparent PowerPoint picture. Register children separately when each part must move independently.

## Slide-count contract

Never hard-code 20 slides. Keep the runtime source of truth in the deck, normally `PAGES.length`, and return it from `pageCount()`. The exporter asks the running deck for this number before capture, so 1, 7, 20, 37, or more slides use the same command.

Update page totals, navigation limits, and progress bars from `PAGES.length` as well.

## DOM layers

Keep exact copy as real DOM text. The exporter currently discovers text under `#frame` and `#txt`, independent images under `#stk img` and `#txt img`, and known Haoqi structural components as native shapes.

For new layouts:

- Place editable copy under `#txt`.
- Place independent PNG/JPG/SVG assets under `#stk` or `#txt`.
- Prefer existing card/row/swatch classes for native-shape conversion.
- Treat unsupported complex CSS effects as part of the background unless the exporter is extended deliberately.

## Required delivery workflow

For every generated Haoqi deck:

1. Generate the requested number of slides from content needs, not from the sample count.
2. Register all user-added independent 3D objects.
3. Export:

   ```bash
   python3 scripts/export-haoqi-pptx-editable.py path/to/deck.html \
     -o path/to/deck-editable.pptx --scheme plus
   ```

4. Open the PPTX with `python-pptx` and confirm slide count and non-zero text/picture counts.
5. Render through LibreOffice or PowerPoint and inspect representative slides.
6. Deliver both the interactive HTML deck and editable PPTX.

## Editable boundary

- DOM copy → real PowerPoint text boxes.
- Registered Three.js objects → independent transparent pictures.
- Clay/sticker images → independent pictures.
- Supported grids/cards/lines/swatches → native PowerPoint shapes.
- WebGL lighting, shadows, reflections, and unregistered scenery → one background image per slide.

PowerPoint cannot preserve live WebGL shaders. Continue 3D geometry/material edits in HTML and re-export; continue text, placement, sizing, rotation, deletion, and basic shape styling directly in PowerPoint.
