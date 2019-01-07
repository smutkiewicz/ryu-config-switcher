package studios.aestheticapps.ryupilot

import android.content.Context
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.Volley

class VolleyHelper constructor(context: Context)
{
    val requestQueue: RequestQueue by lazy {
        Volley.newRequestQueue(context.applicationContext)
    }

    companion object
    {
        @Volatile
        private var INSTANCE: VolleyHelper? = null

        fun getInstance(context: Context) =
            INSTANCE ?: synchronized(this)
            {
                INSTANCE ?: VolleyHelper(context).also {
                    INSTANCE = it
                }
            }
    }

    fun <T> addToRequestQueue(req: Request<T>) = requestQueue.add(req)
}

