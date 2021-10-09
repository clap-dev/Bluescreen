from ctypes.wintypes import BOOL, ULONG
import ctypes

ENABLED = BOOL()
RESPONSE = ULONG()

OPTION_SHUTDOWN = 6
SHUTDOWN_PRIVILEGE = 19
STATUS_NOT_IMPLEMENTED = 0xC0000002

class Bluescreen:
    def __init__(self):
        self.ntdll = ctypes.WinDLL('ntdll.dll')

        self._NtRaiseHardError = self.ntdll.NtRaiseHardError
        self._RtlAdjustPrivilege = self.ntdll.RtlAdjustPrivilege

    def bsod(self):
        if self._RtlAdjustPrivilege(
            SHUTDOWN_PRIVILEGE,
            True,
            False,
            ctypes.byref(
                ENABLED
            )
        ) == 0:
            self._NtRaiseHardError(
                STATUS_NOT_IMPLEMENTED,
                0,
                0,
                0,
                OPTION_SHUTDOWN,
                ctypes.byref(
                    RESPONSE
                )
            )

if __name__ == '__main__':
    bluescreen = Bluescreen()
    bluescreen.bsod()
