package studios.aestheticapps.ryupilot

import android.content.Context
import com.android.volley.RequestQueue
import com.android.volley.toolbox.Volley

object VolleyHelper
{
    private var requestQueue: RequestQueue? = null

    fun obtainRequestQueue(context: Context): RequestQueue?
    {
        if (requestQueue == null)
        {
            requestQueue = Volley.newRequestQueue(context)
        }

        return requestQueue
    }

    fun destroyRequestQueue()
    {
        requestQueue?.cancelAll(null)
        requestQueue = null
    }
}