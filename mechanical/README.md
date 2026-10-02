# Mechanical Design

This folder contains the actual RailGard mechanical engineering files.

## Structure

```text
mechanical/
├── cad/
│   ├── assemblies/
│   └── parts/
├── drawings/
│   ├── assembly/
│   ├── parts/
│   ├── exploded_views/
│   ├── dimensions/
│   ├── pdf/
│   └── images/
└── calculations/
```

### What goes where?

- **CAD source:** CATIA / SolidWorks / STEP / other native engineering files
- **Assembly drawings:** complete robot/chassis/arm assembly drawings
- **Part drawings:** individual component drawings
- **Exploded views:** exploded assembly drawings
- **Dimensioned drawings:** detailed dimensioning documents
- **PDF:** PDF exports of technical drawings
- **Images:** PNG/JPG previews for GitHub

### Recommended example

```text
mechanical/
├── cad/
│   └── assemblies/
│       └── RG-CHASSIS-ASM.CATProduct
└── drawings/
    ├── assembly/
    │   └── RG-CHASSIS-ASM.pdf
    └── images/
        └── RG-CHASSIS-ASM.png
```

Keep the native CAD file whenever possible. The PDF is the engineering
document and the PNG/JPG is only the convenient GitHub preview.
