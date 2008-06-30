#
#git clone http://repo.or.cz/r/microdia.git
#
# Conditional build:
%bcond_without	dist_kernel		# without distribution kernel
#

%define	snap	20080630

Summary:	Linux Driver for Microdia Cameras
Name:		kernel-video-microdia
Version:	0.0.0
Release:	0.%{snap}.1@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://starowa.one.pl/~uzi/pld/microdia-%{snap}.tar.gz
# Source0-md5:	306d8ee4e21e54560c9873619323b1e0
URL:		https://groups.google.com/group/microdia
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
Requires(post,postun):	/sbin/depmod

%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Driver for Microdia Cameras.

This package contains experimental Linux module.

#% description -l pl.UTF-8

%prep
%setup -q -n microdia-%{snap}

%build
%build_kernel_modules -m microdia

%install
rm -rf $RPM_BUILD_ROOT
%install_kernel_modules -m microdia -d kernel/drivers/media/video

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc README
/lib/modules/%{_kernel_ver}/kernel/drivers/media/video/*.ko*
