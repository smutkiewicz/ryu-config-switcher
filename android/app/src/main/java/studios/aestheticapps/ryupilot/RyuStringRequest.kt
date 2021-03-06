package studios.aestheticapps.ryupilot

import android.content.Context
import android.widget.Toast
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.JsonObjectRequest
import org.json.JSONException
import org.json.JSONObject

class RyuStringRequest(private val context: Context, private val settingId: Int)
{
    fun sendPostRequest()
    {
        try
        {
            VolleyHelper
                .getInstance(context)
                .addToRequestQueue(buildJsonObjectRequest())
        }
        catch (e: JSONException)
        {
            e.printStackTrace()
        }
    }

    private fun buildJsonObjectRequest() = object : JsonObjectRequest(
        Request.Method.POST,
        buildUrl(),
        buildJsonBody(),
        Response.Listener<JSONObject> { response -> showToast("Got response: " + response.toString()) },
        Response.ErrorListener { }
    ) { }

    private fun buildJsonBody(): JSONObject
    {
        val jsonBody = JSONObject()
        jsonBody.apply {
            put("Content-Type", "application/json")
            put(PROP_SETTING_ID_NAME, settingId)
        }

        return jsonBody
    }

    private fun buildUrl() = "http://" + PrefsHelper.obtainRyuIpAddress(context) + ":" + RYU_PORT + CHANGE_SETTING_PATH

    private fun showToast(text: String) = Toast.makeText(context, text, Toast.LENGTH_SHORT).show()

    private companion object
    {
        const val CHANGE_SETTING_PATH = "/change_setting/"
        const val PROP_SETTING_ID_NAME = "setting_id"
        const val RYU_PORT = "8181"
    }
}