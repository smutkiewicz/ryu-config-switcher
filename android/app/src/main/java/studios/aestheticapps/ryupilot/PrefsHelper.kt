package studios.aestheticapps.ryupilot

import android.content.Context

object PrefsHelper
{
    private const val PREFS = "prefs"
    private const val PREF_RYU_IP = "ryu_ip"
    private const val DEFAULT_RYU_IP = "127.0.0.1"

    fun obtainRyuIpAddress(context: Context) = context
        .getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        .getString(PREF_RYU_IP, DEFAULT_RYU_IP)

    fun setRyuIpAddress(context: Context, address: String) = putStringValue(context, PREF_RYU_IP, address)

    private fun putStringValue(context: Context, pref: String, value: String)
    {
        context
            .getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(pref, value)
            .apply()
    }
}