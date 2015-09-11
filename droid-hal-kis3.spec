# These and other macros are documented in dhd/droid-hal-device.inc

%define device kis3
%define vendor zte

%define vendor_pretty ZTE
%define device_pretty Kis 3

%define installable_zip 1

%define straggler_files \
/init.class_main.sh\
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}

%include rpm/dhd/droid-hal-device.inc
