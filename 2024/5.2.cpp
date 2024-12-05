#include <bits/stdc++.h>
#define forn(i,i0,n) for(int i = i0; i < n; i++)
typedef long long ll;
using namespace std;
map<ll,set<ll>> g;
int main(){
    ll m; cin >> m;
    while(m--){
        ll a,b; cin >> a >> b;
        g[a].insert(b);
    }
    cout << m << endl;
    ll n; cin >> n;
    ll ans = 0;
    while(n--){
        ll l; cin >> l;
        vector<ll> nums(l);
        for(ll &a: nums) cin >> a;
        bool flag = true;
        set<ll> vis;
        forn(i,0,l){
            for(ll a: g[nums[i]]) flag = flag && !vis.count(a);
            vis.insert(nums[i]);
        }
        if(!flag){
            forn(i,0,l){
                forn(j,0,l-1)
                    if(g[nums[j+1]].count(nums[j])) swap(nums[j],nums[j+1]);
            }
            for(ll a: nums) cout << a << " "; cout << endl;
            ans += nums[(l-1)/2];
        }
    }
    cout << ans << endl;


    return 9;
}