%global _hardened_build 1
%global __provides_exclude_from ^%{_libdir}/weechat/plugins/.*$

Name:      weechat
Summary:   Portable, fast, light and extensible IRC client
Version:   0.4.3
Release:   5%{?dist}
Source:    http://weechat.org/files/src/%{name}-%{version}.tar.bz2
URL:       http://weechat.org
Group:     Applications/Communications
License:   GPLv3

%if 0%{?rhel}
Patch0:    enchant-0.4.3.patch
%endif

BuildRequires: cmake
BuildRequires: docbook-style-xsl
BuildRequires: enchant-devel
BuildRequires: gettext
BuildRequires: gnutls-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: lua-devel
BuildRequires: ncurses-devel
BuildRequires: perl-ExtUtils-Embed
BuildRequires: perl-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: tcl-devel
BuildRequires: zlib-devel

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%package devel
Summary: Development files for weechat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.


%prep
%setup -q -n %{name}-%{version}
%if 0%{?rhel}
%patch0 -p 1
%endif

%build
mkdir build
pushd build
%cmake \
  -DPREFIX=%{_prefix} \
  -DLIBDIR=%{_libdir} \
  -DENABLE_ENCHANT=ON \
  ..
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR="$RPM_BUILD_ROOT"
popd

%find_lang %name


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/en/weechat_faq.en.txt doc/en/weechat_quickstart.en.txt doc/en/weechat_scripting.en.txt
%doc doc/en/weechat_user.en.txt
%{_bindir}/%{name}-curses
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/weechat-plugin.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Wed Apr 09 2014 Russell Golden <niveusluna@niveusluna.org> - 0.4.3-2
- Build and patch for el6
  - This is a _nasty_ hack intended solely to get the binary working.
  - The binary does seem to work whether or not aspell is enabled.

* Sun Feb 16 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-1
- update to upstream release 0.4.3

* Mon Nov 11 2013 Paul Komkoff <i@stingr.net> - 0.4.2-4
- enable enchant detection / aspell build.

* Fri Nov 08 2013 Russell Golden <niveusluna@niveusluna.org> - 0.4.2-3
- Forgot to remove the patch1 instruction

* Fri Nov 08 2013 Russell Golden <niveusluna@niveusluna.org> - 0.4.2-2
- Forgot to remove 0.4.1 from the sources file. (Rawhide only.)

* Fri Nov 08 2013 Russell Golden <niveusluna@niveusluna.org> - 0.4.2-1
- rename binary from "weechat-curses" to "weechat" (with symbolic link "weechat-curses" for compatibility)
- add secured data (encryption of passwords or private data), new command /secure, new file sec.conf
- search of regular expression in buffer with text emphasis, in prefixes, messages or both
- add option "scroll_beyond_end" for command /window
- add optional buffer context in bar items (for example to display bitlbee nicklist in a root bar)
- new options weechat.look.hotlist_{prefix|suffix}
- new option weechat.look.key_bind_safe to prevent any key binding error from user
- new option weechat.network.proxy_curl to use a proxy when downloading URLs with curl
- display day change message dynamically
- support of wildcards in IRC commands (de)op/halfop/voice
- new option irc.look.notice_welcome_redirect to redirect channel welcome notices to the channel buffer
- new option irc.look.nick_color_hash: new hash algorithm to find nick colors (variant of djb2)
- add info about things defined by a script in the detailed view of script (/script show)
- support of "enchant" library in aspell plugin
- many bugs fixed.
- no more man page by default

* Sun Aug 04 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-3
- add BR: libgcrypt-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- update to upstream release 0.4.1
- clean old changelog entries
- fix enchant patch set
- Ruby 2.0 crash now fixed upstream

* Tue Apr 02 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-7
- filter out automatically generated Provides that shouldn't be there (#947399)

* Sat Mar 30 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-6
- enable _hardened_build as weechat matches the "long running" criteria
- remove redundant PIE patch

* Fri Mar 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-5
- fix crash with Ruby 2.0

* Wed Mar 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-4
- rebuild with Ruby 2.0.0
- add patch to properly obtain the version of ruby
- fix bogus dates in older changelog entries

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- reimplement enchant support as a separate patch
- implement additional enchant support for displaying spelling suggestions
  in weechat_aspell_get_suggestions(), which is a new function introduced by
  upstream in 0.4.0

* Mon Jan 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- update to upstream release 0.4.0
- add CMAKE options (DPREFIX and DLIBDIR) which negate the need to patch
- remove enchant patches to keep close to upstream

* Sun Dec 02 2012 Paul Komkoff <i@stingr.net> - 0.3.9.2-2
- add zlib-devel dependency for epel6/ppc build

* Sat Dec  1 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.9.2-1
- new upstream, long overdue

* Mon Nov 19 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.8-4
- fix bz#878025

* Fri Nov 09 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.8-3
- fix bz#875181

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Russell Golden <niveusluna@niveusluna.org> - 0.3.8-1
- New upstream version

* Fri Mar 16 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.7-1
- new upstream version

* Wed Feb 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.6-2
- Rebuilt for Ruby 1.9.3.

* Wed Jan 18 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.6-1
- new upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.3.5-2
- rebuilt

* Thu Jun  2 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.3.5-1
- new upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.3-2
- fixed cmake config to accept python27

* Wed Aug 25 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.3-1
- new upstream version

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri May  7 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.2-2
- spec file fix

* Thu May  6 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.2-1
- new upstream version
