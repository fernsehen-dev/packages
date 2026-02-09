%global commit 01af960984d493006812c935c38626297001849f
%global shortcommit 01af9609
%global gitdate 20260107

Name:          plasma-bigscreen-git
Version:       6.4.80~%{gitdate}.%{shortcommit}
Release:       3%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:       A big launcher giving you access to any installed apps and skills
Url:           https://invent.kde.org/plasma/plasma-bigscreen

# Not currently in the plasma releases. Getting from gitlab tags.
# Source0:       http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source0:       https://invent.kde.org/plasma/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6BluezQt)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Screen)

BuildRequires: cmake(Plasma)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)

BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(QCoro6)

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6WebEngineCore)

Requires:   plasma-workspace-wayland >= %{version}
Requires:   plasma-nano >= %{version}
Requires:   plasma-nm >= %{version}
Requires:   plasma-pa >= %{version}
Requires:   plasma-milou >= %{version}
Requires:   libkscreen >= %{version}
Requires:   kscreen >= %{version}
Requires:   kwin >= %{version}
Requires:   kde-connect >= %{version}

Provides:   %{name}-wayland = %{version}-%{release}

%description
%{summary}


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma-bigscreen --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_mediacenter_{audiodevice,bigscreen_settings,kdeconnect,wifi}.desktop
# desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.uvcviewer.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f plasma-bigscreen.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-bigscreen-{common-env,envmanager,settings,swap-session,uvcviewer,wayland,webapp}
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mediacenter_*.so
%{_kf6_qmldir}/org/kde//bigscreen/
%{_kf6_metainfodir}/org.kde.plasma.bigscreen.metainfo.xml
%{_kf6_datadir}/plasma/look-and-feel/org.kde.plasma.bigscreen/
%{_kf6_datadir}/plasma/plasmoids/org.kde.bigscreen.homescreen/
%{_kf6_datadir}/plasma/shells/org.kde.plasma.bigscreen/
%{_kf6_datadir}/sounds/plasma-bigscreen/
%{_kf6_qtplugindir}/plasma/applets/org.kde.bigscreen.homescreen.so
%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop
# %{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.uvcviewer.desktop
 %{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop


%changelog
* Mon Feb 09 2026 Marcel Mrówka <micro.mail88@gmail.com>
- Initial Release
