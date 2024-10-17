Name:		texlive-piechartmp
Version:	19440
Release:	2
Summary:	Draw pie-charts using MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/piechartmp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The piechartmp package is an easy way to draw pie-charts with
MetaPost. The package implements an interface that enables
users with little MetaPost experience to draw charts. A
highlight of the package is the possibility of suppressing some
segments of the chart, thus creating the possibility of several
charts from the same data.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/piechartmp/piechartmp.mp
%doc %{_texmfdistdir}/doc/metapost/piechartmp/INSTALL
%doc %{_texmfdistdir}/doc/metapost/piechartmp/LEGAL
%doc %{_texmfdistdir}/doc/metapost/piechartmp/README
%doc %{_texmfdistdir}/doc/metapost/piechartmp/README.TEXLIVE
%doc %{_texmfdistdir}/doc/metapost/piechartmp/examples/wec-mfun.mp
%doc %{_texmfdistdir}/doc/metapost/piechartmp/examples/wec-mfun.pdf
%doc %{_texmfdistdir}/doc/metapost/piechartmp/examples/wec.mp
%doc %{_texmfdistdir}/doc/metapost/piechartmp/examples/wec.pdf
%doc %{_texmfdistdir}/doc/metapost/piechartmp/examples/worldmap.jpg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
