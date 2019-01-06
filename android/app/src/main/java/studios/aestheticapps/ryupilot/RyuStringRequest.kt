package studios.aestheticapps.ryupilot

import android.content.Context
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.Volley
import org.json.JSONException
import org.json.JSONObject

class RyuStringRequest
{
    private fun sendPostRequest(context: Context)
    {
        try
        {
            val requestQueue = Volley.newRequestQueue(context)
            val URL = ""
            val jsonBody = JSONObject()

            jsonBody.put("property", "1")

            val jsonObject = object : JsonObjectRequest(
                Request.Method.POST, URL, jsonBody,
                Response.Listener<JSONObject> { response -> },
                Response.ErrorListener { }
            ) {}

            VolleyHelper.obtainRequestQueue(context)?.add(jsonObject)
        }
        catch (e: JSONException)
        {
            e.printStackTrace()
        }
    }
}