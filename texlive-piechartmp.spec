# revision 19440
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/piechartmp
# catalog-date 2007-01-13 20:56:44 +0100
# catalog-license lppl
# catalog-version 0.3.0
Name:		texlive-piechartmp
Version:	0.3.0
Release:	1
Summary:	Draw pie-charts using MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/piechartmp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piechartmp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The piechartmp package is an easy way to draw pie-charts with
MetaPost. The package implements an interface that enables
users with little MetaPost experience to draw charts. A
highlight of the package is the possibility of suppressing some
segments of the chart, thus creating the possibility of several
charts from the same data.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
