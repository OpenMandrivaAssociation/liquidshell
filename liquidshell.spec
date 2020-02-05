Name:           liquidshell
Version:        1.5
Release:        1
Summary:        Alternative desktop replacement for Plasma, Qt and KF5 based
License:        GPL-3.0
Group:          System/GUI/KDE
URL:            https://github.com/KDE/liquidshell
Source:         https://github.com/KDE/liquidshell/archive/VERSION_%{version}/%{name}-VERSION_%{version}.tar.gz
Patch0:         liquidshell-compile-with-new-qt-kde-openmandriva.patch

BuildRequires:  pkgconfig(packagekitqt5)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

%description
liquidshell is a basic Desktop Shell implemented using QtWidgets. 
Alternative desktop replacement for Plasma, Qt and KF5 based. 
It using QtWidgets instead of QtQuick to ensure hardware acceleration is not required

Main Features:
- Wallpaper per virtual desktop
- Weather, Disk Usage, Picture Frame Applets (per virtual desktop or on all)
- No animations, low memory and CPU footprint
- Instant startup
- QtWidgets based, therefore follows widget style from systemsettings
- Icons are used from your globally defined icon theme from systemsettings
- Colors are used from your globally defined color theme from systemsettings
- Can additionally be styled with css by passing the commandline option -stylesheet filename.css
  (see included example stylesheet.css)
- uses existing KDE Frameworks dialogs for most configurations, e.g. StartMenu, Virtual Desktops, Bluetooth, Network
- Just one bottom DesktopPanel, containing:
  StartMenu (allowing drag of entries into konqueror/dolphin to configure QuickLaunch or AppMenu entries)
  QuickLaunch (showing icons for .desktop files from a configurable folder)
  AppMenu (showing .desktop files in a menu from a configurable folder, defaults to users desktop folder)
  Pager (for switching virtual desktops)
  WindowList (Popup showing all open windows on all desktops)
  TaskBar (showing windows on the current desktop, allowing drag of an entry onto the Pager to move to a different desktop)
  LockLogout

%prep
%setup -qn %{name}-VERSION_%{version}
%autopatch -p0

%build
%cmake_kde5
%ninja_build

%install
%ninja_install -C build

%files
%doc README
%license COPYING
%{_bindir}/liquidshell
%{_datadir}/applications/org.kde.liquidshell.desktop
%{_iconsdir}/icons/hicolor/48x48/apps/liquidshell.png
%{_datadir}/knotifications5/liquidshell.notifyrc
