Name:           liquidshell
Version:        1.10.0
Release:        1
Summary:        Alternative desktop replacement for Plasma, Qt and KF6 based
License:        GPL-3.0
Group:          System/GUI/KDE
URL:            https://github.com/KDE/liquidshell
Source0:         https://invent.kde.org/system/liquidshell/-/archive/v%{version}/liquidshell-v%{version}.tar.bz2

BuildRequires:  pkgconfig(packagekitqt6)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6Widgets)
#BuildRequires:  cmake(Qt5X11Extras)
#BuildRequires:  cmake(Qt6ThemeSupport)

%description
liquidshell is a basic Desktop Shell implemented using QtWidgets. 
Alternative desktop replacement for Plasma, Qt and KF6 based. 
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
%autosetup -n %{name}-v%{version} -p1

%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/liquidshell
%{_bindir}/start_liquidshell
%{_datadir}/applications/org.kde.liquidshell.desktop
%{_iconsdir}/hicolor/*/apps/liquidshell.png
%{_datadir}/knotifications5/liquidshell.notifyrc
%{_datadir}/xsessions/%{name}-session.desktop
%{_datadir}/metainfo/org.kde.liquidshell.appdata.xml
