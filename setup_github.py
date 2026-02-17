#!/usr/bin/env python3
"""
GitHub Presentation Setup Script
Untuk Laporan PKL - Kelvin
SMK Negeri 1 Sumarorong
"""

import os
import shutil
from pathlib import Path

def create_github_structure():
    """Membuat struktur folder untuk GitHub repository"""
    
    print("=" * 60)
    print("SETUP GITHUB PRESENTATION")
    print("Laporan PKL - CV Sinar Alam Motor")
    print("=" * 60)
    print()
    
    # Base directory
    base_dir = Path("/home/claude/github-presentation")
    
    # Struktur folder
    folders = [
        base_dir / "images",
        base_dir / ".github" / "workflows",
        base_dir / "docs",
        base_dir / "assets"
    ]
    
    print("📁 Membuat struktur folder...")
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {folder.relative_to(base_dir)}/")
    
    print()
    print("✅ Struktur folder berhasil dibuat!")
    print()
    
    return base_dir

def create_gitignore():
    """Membuat .gitignore file"""
    
    print("📝 Membuat .gitignore...")
    
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
*.log

# Build
build/
dist/
*.egg-info/
"""
    
    with open("/home/claude/github-presentation/.gitignore", "w") as f:
        f.write(gitignore_content)
    
    print("   ✓ .gitignore created")
    print()

def create_license():
    """Membuat LICENSE file"""
    
    print("📄 Membuat LICENSE...")
    
    license_content = """MIT License

Copyright (c) 2025 Kelvin - SMK Negeri 1 Sumarorong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    with open("/home/claude/github-presentation/LICENSE", "w") as f:
        f.write(license_content)
    
    print("   ✓ LICENSE created")
    print()

def create_github_actions():
    """Membuat GitHub Actions workflow untuk auto-deploy"""
    
    print("⚙️ Membuat GitHub Actions workflow...")
    
    workflow_content = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Pages
        uses: actions/configure-pages@v4
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""
    
    workflow_path = Path("/home/claude/github-presentation/.github/workflows")
    workflow_path.mkdir(parents=True, exist_ok=True)
    
    with open(workflow_path / "deploy.yml", "w") as f:
        f.write(workflow_content)
    
    print("   ✓ GitHub Actions workflow created")
    print()

def create_contributing():
    """Membuat CONTRIBUTING.md"""
    
    print("📝 Membuat CONTRIBUTING.md...")
    
    contributing_content = """# Contributing to Laporan PKL

Terima kasih atas minat Anda untuk berkontribusi pada repository ini!

## Cara Berkontribusi

1. **Fork** repository ini
2. **Clone** fork Anda: `git clone https://github.com/YOUR-USERNAME/pkl-laporan.git`
3. **Create branch**: `git checkout -b feature/YourFeature`
4. **Commit** perubahan: `git commit -m 'Add some feature'`
5. **Push** ke branch: `git push origin feature/YourFeature`
6. **Submit** Pull Request

## Pedoman

- Gunakan bahasa yang jelas dan mudah dipahami
- Sertakan dokumentasi untuk perubahan besar
- Test semua perubahan sebelum submit PR
- Follow struktur kode yang ada

## Kode Etik

- Bersikap hormat dan profesional
- Berikan feedback yang konstruktif
- Fokus pada perbaikan, bukan kritik personal

## Pertanyaan?

Jika ada pertanyaan, silakan buka Issue atau hubungi maintainer.

---

*Happy Contributing! 🎉*
"""
    
    with open("/home/claude/github-presentation/CONTRIBUTING.md", "w") as f:
        f.write(contributing_content)
    
    print("   ✓ CONTRIBUTING.md created")
    print()

def create_setup_instructions():
    """Membuat SETUP.md dengan instruksi lengkap"""
    
    print("📖 Membuat SETUP.md...")
    
    setup_content = """# 🚀 Setup Instructions

Panduan lengkap untuk mengatur GitHub repository dan GitHub Pages.

## 📋 Prasyarat

- Akun GitHub
- Git terinstall di komputer
- Text editor (VSCode, Sublime, dll)

## 🔧 Langkah Setup

### 1. Buat Repository GitHub

1. Login ke [GitHub](https://github.com)
2. Klik tombol **New repository** atau kunjungi https://github.com/new
3. Isi detail repository:
   - **Repository name**: `pkl-laporan` (atau nama lain)
   - **Description**: "Laporan PKL di CV Sinar Alam Motor - SMK Negeri 1 Sumarorong"
   - **Visibility**: Public ✅
   - **Initialize**: Jangan centang "Add README" (kita sudah punya)
4. Klik **Create repository**

### 2. Upload Files ke GitHub

#### Opsi A: Via GitHub Web (Mudah)

1. Di halaman repository baru, klik **uploading an existing file**
2. Drag & drop semua file dari folder `github-presentation`:
   - README.md
   - index.html
   - LICENSE
   - .gitignore
   - Folder `images/` (dengan semua foto)
   - Folder `.github/` (dengan workflows)
   - File `Laporan_PKL_Kelvin_LENGKAP_ENHANCED.docx`
3. Scroll ke bawah, tambahkan commit message: "Initial commit"
4. Klik **Commit changes**

#### Opsi B: Via Git Command Line (Advanced)

```bash
# Navigate ke folder
cd /home/claude/github-presentation

# Initialize git
git init

# Add remote
git remote add origin https://github.com/USERNAME/pkl-laporan.git

# Add all files
git add .

# Commit
git commit -m "Initial commit: Laporan PKL"

# Push
git branch -M main
git push -u origin main
```

### 3. Aktifkan GitHub Pages

1. Di repository, klik **Settings** (⚙️)
2. Di menu kiri, klik **Pages**
3. Di bagian **Source**:
   - Branch: `main`
   - Folder: `/ (root)`
4. Klik **Save**
5. Tunggu 1-2 menit untuk deployment
6. Refresh halaman, akan muncul link: `https://username.github.io/pkl-laporan`

### 4. Verifikasi

✅ Buka link GitHub Pages Anda  
✅ Pastikan navigasi berfungsi  
✅ Cek semua gambar muncul  
✅ Test tombol download  

## 🎨 Kustomisasi

### Mengubah Warna

Edit file `index.html`, cari bagian CSS:

```css
/* Gradient utama */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Ganti dengan warna Yamaha jika mau */
background: linear-gradient(135deg, #0033A0 0%, #E60012 100%);
```

### Menambah Konten

1. Edit `index.html` untuk menambah section baru
2. Edit `README.md` untuk menambah informasi
3. Commit & push perubahan

## 📱 Sharing

Share link GitHub Pages Anda:

```
🔗 https://username.github.io/pkl-laporan
```

Atau buat QR Code untuk presentasi!

## ❓ Troubleshooting

### Gambar tidak muncul?
- Pastikan folder `images/` ter-upload
- Check path di HTML (case-sensitive)

### GitHub Pages tidak aktif?
- Pastikan repository public
- Check Settings > Pages sudah diaktifkan
- Tunggu 5-10 menit untuk propagasi

### File .docx tidak bisa didownload?
- Pastikan file ada di root directory
- Check link path di HTML

## 📞 Support

Butuh bantuan? Open an Issue di repository!

---

**Good luck! 🚀**
"""
    
    with open("/home/claude/github-presentation/SETUP.md", "w") as f:
        f.write(setup_content)
    
    print("   ✓ SETUP.md created")
    print()

def copy_docx_file():
    """Copy file DOCX ke folder presentation"""
    
    print("📄 Menyalin file DOCX...")
    
    source = "/mnt/user-data/outputs/Laporan_PKL_Kelvin_LENGKAP_ENHANCED.docx"
    dest = "/home/claude/github-presentation/Laporan_PKL_Kelvin_LENGKAP_ENHANCED.docx"
    
    if os.path.exists(source):
        shutil.copy2(source, dest)
        print(f"   ✓ File copied to {dest}")
    else:
        print(f"   ⚠️ Source file not found: {source}")
    
    print()

def create_deployment_script():
    """Membuat script untuk easy deployment"""
    
    print("🚀 Membuat deployment script...")
    
    deploy_script = """#!/bin/bash

# Deployment Script for GitHub
# Laporan PKL - Kelvin

echo "================================"
echo "GITHUB DEPLOYMENT SCRIPT"
echo "================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed!"
    echo "Please install git first: sudo apt install git"
    exit 1
fi

echo "📦 Preparing repository..."

# Initialize git if not already
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git initialized"
fi

# Add all files
git add .
echo "✓ Files staged"

# Commit
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Update laporan PKL"
fi

git commit -m "$commit_msg"
echo "✓ Changes committed"

# Push
read -p "Enter your GitHub username: " username
read -p "Enter repository name (e.g., pkl-laporan): " repo_name

git branch -M main

# Check if remote already exists
if git remote | grep -q "origin"; then
    echo "✓ Remote already configured"
else
    git remote add origin "https://github.com/$username/$repo_name.git"
    echo "✓ Remote added"
fi

echo ""
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo ""
echo "================================"
echo "✅ DEPLOYMENT COMPLETE!"
echo "================================"
echo ""
echo "Your site will be available at:"
echo "https://$username.github.io/$repo_name"
echo ""
echo "Note: It may take 1-2 minutes for GitHub Pages to update."
"""
    
    script_path = "/home/claude/github-presentation/deploy.sh"
    with open(script_path, "w") as f:
        f.write(deploy_script)
    
    # Make executable
    os.chmod(script_path, 0o755)
    
    print("   ✓ deploy.sh created (executable)")
    print()

def create_quick_start():
    """Membuat QUICKSTART.md"""
    
    print("⚡ Membuat QUICKSTART.md...")
    
    quickstart = """# ⚡ Quick Start Guide

Cara tercepat untuk get started dengan presentasi GitHub ini!

## 🎯 Langkah Cepat (5 Menit)

### 1️⃣ Upload ke GitHub (2 menit)

1. Buka https://github.com/new
2. Nama repository: `pkl-laporan`
3. Public ✅
4. Create repository
5. Upload semua file dari folder `github-presentation`

### 2️⃣ Aktifkan Pages (1 menit)

1. Settings → Pages
2. Source: `main` branch, `/ (root)` folder
3. Save

### 3️⃣ Akses! (2 menit)

Tunggu 1-2 menit, buka:
```
https://USERNAME.github.io/pkl-laporan
```

## 🎉 Done!

Sekarang presentasi Anda sudah online dan bisa diakses dari mana saja!

## 📱 Tips

- Share link ke teman/guru
- Buat QR Code untuk presentasi
- Tambahkan ke LinkedIn/portfolio
- Bookmark untuk referensi

## 🆘 Butuh Bantuan?

Lihat [SETUP.md](SETUP.md) untuk panduan lengkap!

---

*Happy Presenting! 🚀*
"""
    
    with open("/home/claude/github-presentation/QUICKSTART.md", "w") as f:
        f.write(quickstart)
    
    print("   ✓ QUICKSTART.md created")
    print()

def generate_summary():
    """Generate summary report"""
    
    print()
    print("=" * 60)
    print("✅ SETUP SELESAI!")
    print("=" * 60)
    print()
    
    print("📦 Files yang dibuat:")
    files = [
        "README.md - Dokumentasi utama dengan navigasi lengkap",
        "index.html - Presentasi interaktif dengan tombol navigasi",
        "LICENSE - MIT License",
        ".gitignore - Git ignore rules",
        "CONTRIBUTING.md - Panduan kontribusi",
        "SETUP.md - Instruksi setup lengkap",
        "QUICKSTART.md - Panduan quick start",
        "deploy.sh - Script deployment otomatis",
        ".github/workflows/deploy.yml - Auto-deploy GitHub Actions",
        "images/ - 8 foto dokumentasi kegiatan PKL",
        "Laporan_PKL_Kelvin_LENGKAP_ENHANCED.docx - Laporan lengkap"
    ]
    
    for i, file in enumerate(files, 1):
        print(f"   {i:2d}. ✓ {file}")
    
    print()
    print("=" * 60)
    print("🚀 CARA MENGGUNAKAN:")
    print("=" * 60)
    print()
    print("1. Upload semua file ke GitHub repository baru")
    print("2. Aktifkan GitHub Pages di Settings")
    print("3. Akses presentasi di: https://username.github.io/repo-name")
    print()
    print("Lihat QUICKSTART.md atau SETUP.md untuk panduan detail!")
    print()
    print("=" * 60)
    print("📁 Lokasi files: /home/claude/github-presentation/")
    print("=" * 60)
    print()

def main():
    """Main function"""
    
    # Create structure
    base_dir = create_github_structure()
    
    # Create all files
    create_gitignore()
    create_license()
    create_github_actions()
    create_contributing()
    create_setup_instructions()
    create_deployment_script()
    create_quick_start()
    
    # Copy DOCX
    copy_docx_file()
    
    # Generate summary
    generate_summary()
    
    print("✨ Semua siap! Repository GitHub presentation sudah lengkap!")
    print()

if __name__ == "__main__":
    main()
