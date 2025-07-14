#
# TODO:
# - BRs
# - Rs and check existing one
# - patch easygui's code to run egdesigner from different location
#
Summary:	A GUI for everything
Summary(pl.UTF-8):	GUI do wszystkiego
Name:		everygui
Version:	0.99.b
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/everygui/%{name}-%{version}.tar.gz
# Source0-md5:	78953de66b973b97b194d679969acc9f
Patch0:		%{name}-setup.patch
Patch1:		%{name}-exec.patch
URL:		http://everygui.sourceforge.net/
BuildRequires:	python-pygtk-gtk >= 2:2.6
Requires:	python >= 2.3
Requires:	python-pygtk-libglade >= 2:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EveryGui is an attempt at being a GTK+ Graphical User Interface for
"Everything" (involving command line programs) on UNIX systems. This
goal is achieved by providing two powerful applications:

Chameleon, which is a dynamic GUI for virtually any tool or OS
command. It loads config files of tools which are chosen from a list,
and dynamically creates widgets reperesenting the tools' options. Not
only does it execute the commands, but it can save a batch of commands
into a shell script for later/repeated use.

And Designer, which is a visual environment for creating/editing
config files that determine Chameleon's different behaviours for each
tool/command. Designer feels like a cross between QT Designer and
Glade, but requires no coding at all to get the functionality working
(that's Chameleon's job to do it automagically).

%description -l pl.UTF-8
EveryGui to jest próbą stworzenia GUI w GTK+ do "wszystkiego"
(związanego z programami działającymi z linii poleceń) na systemach
UNIX. Cel osiągnięto dostarczając dwóch potężnych aplikacji:

Chameleona, który jest dynamicznym GUI dla niemalże każdego
narzędzia albo komendy systemowej. Ładuje pliki konfiguracyjne
narzędzi wybranych z listy i dynamicznie tworzy kontrolki
reprezentujące przełączniki narzędzia. Chameleon nie tylko
wywołuje komendy ale i również może zachować serię komend w
pliku powłoki dla późniejszego/powtarzającego się użycia.

I Designera, który jest wizualnym środowiskiem do tworzenia/edycji
plików konfiguracyjnych, które powodują różne zachowanie
Chameleona dla każdego narzędzia/polecenia. Designer przypomina w
zachowaniu mieszankę Qt Designera i Glade'a, ale nie wymaga żadnego
programowania do uruchomienia funkcjonalności (to w końcu zadanie
Chameleona, aby robić to automagicznie).

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1

%build
cat << EOF > everygui
#!/bin/sh

#start everygui
%{__python} %{py_sitescriptdir}/everygui/everygui.pyc
EOF

cat << EOF > egdesign
#!/bin/sh

#start designer
%{__python} %{py_sitescriptdir}/everygui/designer.pyc
EOF

%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/everygui
%dir %{py_sitescriptdir}/everygui
%{py_sitescriptdir}/everygui/*.py[co]
%{py_sitescriptdir}/everygui-%{version}-*.egg-info
