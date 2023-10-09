package 홀짝구분하기
fun main() {
    val solution =  Solution()
    solution.run(arrayOf("1", "3", "0"))
}
class Solution {
    fun run(args: Array<String>) {
        for(arg in args) {
            val a = arg!!.toInt()
            val result: String = if (a % 2 == 0) "even" else "odd"
            println("$a is $result")
        }
    }
}