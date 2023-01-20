# Convert images to PDF

`convertToPDF.py` is a script that searches files in a folder given by the command line and join them, in alphabethical order, in a PDF format using the tool `convert` from Linux.

`convertSubFoldersToPDF.py` receives a path to a folder containing sub-folders where the same process as the previous script would be applied.

## Setup

You may have to setup a few things first. First install the tool `convert` from ImageMagick and then allow the production of PDF files.

### Install convert in Ubuntu

```bash
sudo apt install imagemagick
```

### Add PDF security policy

Add `<policy domain="coder" rights="read | write" pattern="PDF" />` before `</policymap>` in `/etc/ImageMagick-7/policy.xml` file.





## How to run

```
python3 convertToPDF.py <folder>
```

<folder> is the path to the folder that contains the images to be merged into a pdf.
