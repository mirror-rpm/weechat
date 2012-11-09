Name:      weechat
Summary:   Portable, fast, light and extensible IRC client
Version:   0.3.8
Release:   3%{?dist}
Source:    http://weechat.org/files/src/%{name}-%{version}.tar.bz2
Patch0:    weechat-combined.patch
Patch1:    weechat-fix-0.patch
URL:       http://weechat.org
Group:     Applications/Communications
License:   GPLv3
BuildRequires: ncurses-devel python-devel perl-devel ruby-devel 
BuildRequires: gnutls-devel lua-devel enchant-devel
BuildRequires: docbook-style-xsl gettext ruby
BuildRequires: cmake perl-ExtUtils-Embed tcl-devel
BuildRequires: libcurl-devel

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%package devel
Summary: Development files for weechat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%find_lang %name

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/en/weechat_faq.en.txt doc/en/weechat_quickstart.en.txt doc/en/weechat_scripting.en.txt
%doc doc/en/weechat_user.en.txt
%{_mandir}/man1/%{name}-curses.1*
%{_bindir}/%{name}-curses
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/weechat-plugin.h
%{_libdir}/pkgconfig/*.pc

%changelog
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

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.3.0-3
- rebuild against perl 5.10.1

* Sat Nov 28 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.3.0-2
- use enchant as spelling provider (instead of aspell), patch by Caolan McNamara

* Thu Sep 10 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.3.0-1
- new, shiny version
- new cmake-based build

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.3-1
- gnutls detection bugfix

* Fri May  1 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.2-1
- fix some charset decoding problems.

* Thu Mar 19 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.1-1
- fix bz#490709

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.6-6
- Rebuild for Python 2.6

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.2.6-5
- Fix Patch0:/%%patch mismatch.

* Fri Jun 27 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-4
- rebuild because of ssl/tls deps

* Sun Feb 24 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-3
- make weechat-curses a PIE
- remove irrelevant INSTALL from docs
- remove *.la from plugins

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.6-2
- Autorebuild for GCC 4.3

* Fri Oct 19 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-1
- new upstream version, new license
* Fri Jun  8 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.5-1
- new upstream version
* Mon Apr  9 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.4-2
- preparing for Fedora

* Thu Mar 29 2007 FlashCode <flashcode@flashtux.org> 0.2.4-1
- Released version 0.2.4
* Wed Jan 10 2007 FlashCode <flashcode@flashtux.org> 0.2.3-1
- Released version 0.2.3
* Sat Jan 06 2007 FlashCode <flashcode@flashtux.org> 0.2.2-1
- Released version 0.2.2
* Sun Oct 01 2006 FlashCode <flashcode@flashtux.org> 0.2.1-1
- Released version 0.2.1
* Sat Aug 19 2006 FlashCode <flashcode@flashtux.org> 0.2.0-1
- Released version 0.2.0
* Thu May 25 2006 FlashCode <flashcode@flashtux.org> 0.1.9-1
- Released version 0.1.9
* Sat Mar 18 2006 FlashCode <flashcode@flashtux.org> 0.1.8-1
- Released version 0.1.8
* Sat Jan 14 2006 FlashCode <flashcode@flashtux.org> 0.1.7-1
- Released version 0.1.7
* Fri Nov 11 2005 FlashCode <flashcode@flashtux.org> 0.1.6-1
- Released version 0.1.6
* Sat Sep 24 2005 FlashCode <flashcode@flashtux.org> 0.1.5-1
- Released version 0.1.5
* Sat Jul 30 2005 FlashCode <flashcode@flashtux.org> 0.1.4-1
- Released version 0.1.4
* Sat Jul 02 2005 FlashCode <flashcode@flashtux.org> 0.1.3-1
- Released version 0.1.3
* Sat May 21 2005 FlashCode <flashcode@flashtux.org> 0.1.2-1
- Released version 0.1.2
* Sat Mar 20 2005 FlashCode <flashcode@flashtux.org> 0.1.1-1
- Released version 0.1.1
* Sat Feb 12 2005 FlashCode <flashcode@flashtux.org> 0.1.0-1
- Released version 0.1.0
* Sat Jan 01 2005 FlashCode <flashcode@flashtux.org> 0.0.9-1
- Released version 0.0.9
* Sat Oct 30 2004 FlashCode <flashcode@flashtux.org> 0.0.8-1
- Released version 0.0.8
* Sat Aug 08 2004 FlashCode <flashcode@flashtux.org> 0.0.7-1
- Released version 0.0.7
* Sat Jun 05 2004 FlashCode <flashcode@flashtux.org> 0.0.6-1
- Released version 0.0.6
* Thu Feb 02 2004 FlashCode <flashcode@flashtux.org> 0.0.5-1
- Released version 0.0.5
* Thu Jan 01 2004 FlashCode <flashcode@flashtux.org> 0.0.4-1
- Released version 0.0.4
* Mon Nov 03 2003 FlashCode <flashcode@flashtux.org> 0.0.3-1
- Released version 0.0.3
* Sun Oct 05 2003 FlashCode <flashcode@flashtux.org> 0.0.2-1
- Released version 0.0.2
* Sat Sep 27 2003 FlashCode <flashcode@flashtux.org> 0.0.1-1
- Released version 0.0.1
