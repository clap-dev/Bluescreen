# Bluescreen of Death

This is a very basic implementation on how to replicate a BSOD (Bluescreen of Death), using Python and Ctypes.

![screen-gif](https://clap.shx.gg/5ceQmzjWx.gif)

## Usage

```bash
python bluescreen.py
```

## How does it work?

I won't go too far into detail as this is pretty basic. We are calling [RtlAdjustPrivilege](http://pinvoke.net/default.aspx/ntdll/RtlAdjustPrivilege.html) to give our process shutdown privileges. After that, we raise a [STATUS_NOT_IMPLEMENTED](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55#STATUS_NOT_IMPLEMENTED) error with [NtRaiseHardError](http://pinvoke.net/default.aspx/ntdll/NtRaiseHandError.html), essentially telling our computer that there was an issue and a status was not completed. This causes a BSOD as when we call [NtRaiseHardError](http://pinvoke.net/default.aspx/ntdll/NtRaiseHandError.html), it internally sends a [HARDERROR_MSG](http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FError%2FHARDERROR_MSG.html) to the [Local Inter-Process Communication Server](http://zezula.net/en/prog/lpc.html), resulting in a BSOD.

## Sources

1) [RtlAdjustPrivilege](http://pinvoke.net/default.aspx/ntdll/RtlAdjustPrivilege.html)

2) [NtRaiseHardError](http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FError%2FNtRaiseHardError.html)

3) [STATUS_NOT_IMPLEMENTED](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55#STATUS_NOT_IMPLEMENTED)

4) [HARDERROR_MSG](http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FError%2FHARDERROR_MSG.html)

5) [Local Inter-Process Communication Server](http://zezula.net/en/prog/lpc.html)
